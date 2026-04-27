import os
import pandas as pd

from ollama import ollama_generate

DATA_DIR = "data"
TOPICS_FILE = f"{DATA_DIR}/topics.csv"

TOPICS_PROMPT_TEMPLATE = (
    "Generate {count} unique Python problem topic titles (3-7 words each). "
    "Focus on simple, beginner-level practice problems suitable for school or exercises (examples: prime number check, sum of digits, reverse string, FizzBuzz, factorial). "
    "Each title should be short and specific. One line = one title. DO NOT add numbers, descriptions, or extra text. Avoid duplicates and near-synonyms."
)

os.makedirs(DATA_DIR, exist_ok=True)


def _normalize_title(s: str) -> str:
    import re
    s = s.strip().lower()
    s = re.sub(r"[^a-z0-9\s]", "", s)
    s = re.sub(r"\s+", " ", s)
    return s


def load_or_generate_topics(num_topics=50, temperature=0.8, force=False, max_attempts=60):
    """Load existing topics.csv or generate until we have at least `num_topics` titles.

    - If `force` is True, regenerate from scratch.
    - Uses the model to generate missing titles and deduplicates them.
    """
    existing = []
    if os.path.exists(TOPICS_FILE) and not force:
        try:
            df = pd.read_csv(TOPICS_FILE)
            existing = [str(x).strip() for x in df["topic"].tolist() if str(x).strip()]
        except Exception:
            existing = []

    titles = []
    seen = set(_normalize_title(t) for t in existing)
    titles.extend(existing)

    attempts = 0
    while len(titles) < num_topics and attempts < max_attempts:
        remaining = num_topics - len(titles)
        # request exactly 10 topics per prompt to keep prompts small
        to_request = min(10, remaining)
        prompt = TOPICS_PROMPT_TEMPLATE.format(count=to_request)
        text = ollama_generate(prompt, temperature)
        attempts += 1

        if not text:
            continue

        new_items = [t.strip("- ").strip() for t in text.split("\n") if t.strip()]
        for it in new_items:
            key = _normalize_title(it)
            if key in seen:
                continue
            seen.add(key)
            titles.append(it)
            if len(titles) >= num_topics:
                break

    if len(titles) < num_topics:
        print(f"Warning: only generated {len(titles)} topics out of requested {num_topics}")

    df_out = pd.DataFrame({
        "topic_id": range(len(titles)),
        "topic": titles[:num_topics]
    })
    df_out.to_csv(TOPICS_FILE, index=False)
    return df_out
