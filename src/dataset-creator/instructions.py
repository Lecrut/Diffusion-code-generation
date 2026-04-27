import os
import pandas as pd
from tqdm import tqdm

from ollama import ollama_generate

DATA_DIR = "data"
INSTR_FILE = f"{DATA_DIR}/instructions.csv"

INSTRUCTIONS_PROMPT_TEMPLATE = (
    "For the topic: \"{topic}\" generate {n} unique, detailed implementation instructions. "
    "Each instruction should include: a short task description (what to do), exact input/output (data types), implementation requirements: modularity (split into functions), no magic numbers (use named constants), no global state, clear names and type hints, optional performance constraints or implementation style (e.g., recursion, DP, generators). "
    "One line = one instruction. Do not add explanations or examples."
)

os.makedirs(DATA_DIR, exist_ok=True)


def _normalize_instr(s: str) -> str:
    import re
    s = s.strip().lower()
    s = re.sub(r"[^a-z0-9\s]", " ", s)
    s = re.sub(r"\s+", " ", s)
    return s


def load_or_generate_instructions(topics_df, instr_per_topic=5, temperature=0.9, force=False, max_attempts_per_topic=8):
    """Ensure exactly `instr_per_topic` unique instructions per topic.

    If `INSTR_FILE` exists and `force` is False, it will load and only fill missing instructions for topics.
    """
    existing = {}
    if os.path.exists(INSTR_FILE) and not force:
        try:
            df_existing = pd.read_csv(INSTR_FILE)
            for _, r in df_existing.iterrows():
                tid = int(r["topic_id"]) if "topic_id" in r else None
                existing.setdefault(tid, []).append(str(r["instruction"]))
        except Exception:
            existing = {}

    rows = []
    for _, row in tqdm(topics_df.iterrows(), total=len(topics_df)):
        tid = int(row["topic_id"])
        topic = row["topic"]
        current = existing.get(tid, [])[:]
        seen = set(_normalize_instr(x) for x in current)

        attempts = 0
        while len(current) < instr_per_topic and attempts < max_attempts_per_topic:
            need = instr_per_topic - len(current)
            request_n = min(10, need)
            prompt = INSTRUCTIONS_PROMPT_TEMPLATE.format(topic=topic, n=request_n)
            text = ollama_generate(prompt, temperature)
            attempts += 1
            if not text:
                continue

            candidates = [i.strip("- ").strip() for i in text.splitlines() if i.strip()]
            for cand in candidates:
                key = _normalize_instr(cand)
                if key in seen:
                    continue
                seen.add(key)
                current.append(cand)
                if len(current) >= instr_per_topic:
                    break

        # if still not enough, fill with placeholders noting missing
        while len(current) < instr_per_topic:
            current.append(f"[MISSING INSTRUCTION for topic: {topic}]")

        for i, instr in enumerate(current[:instr_per_topic]):
            rows.append({
                "topic_id": tid,
                "instruction_id": i,
                "topic": topic,
                "instruction": instr
            })

    df = pd.DataFrame(rows)
    df.to_csv(INSTR_FILE, index=False)
    return df
