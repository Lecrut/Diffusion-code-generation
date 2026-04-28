import os
import random
import re
import pandas as pd

from ollama import ollama_generate 

DATA_DIR = "data"
TOPICS_FILE = f"{DATA_DIR}/topics.csv"

TOPICS_TEMPERATURES = [i * 0.05 for i in range(21)]

TOPICS_CATEGORIES = [
    "math operations",
    "string manipulation",
    "list methods",
    "boolean logic",
    "dictionary basics",
    "simple geometry",
    "time and dates",
    "unit conversions (abstract)",
    "basic statistics (mean, min, max)",
    "loop patterns",
    "conditional logic",
    "text parsing",
    "simple I/O simulations",
    "array indexing",
    "shape and area",
]

TOPICS_PROMPT_TEMPLATE = (
    "Generate {count} unique Python programming task titles for beginners.\n"
    "CATEGORY: {category}.\n"
    "RULES:\n"
    "1. Focus on very simple, school-level logic.\n"
    "2. Use 3-7 words per title.\n"
    "3. ABSOLUTELY NO numbers or specific data in titles (e.g., use 'Compare two numbers' instead of 'Is 5 greater than 3').\n"
    "4. No numbering, no bullet points, no descriptions.\n"
    "5. Each title must be a standalone coding challenge.\n"
    "Output only the titles, one per line.\n"
    "Always return at least one valid title and never output an empty response."
)

os.makedirs(DATA_DIR, exist_ok=True)


def _normalize_title(s: str) -> str:
    s = s.strip().lower()
    s = re.sub(r"[^a-z0-9\s]", "", s)
    s = re.sub(r"\s+", " ", s)
    return s


def _valid_title(title: str) -> bool:
    clean = title.strip()
    if not clean:
        return False
    
    if re.search(r"\d", clean):
        return False
        
    clean = re.sub(r"[^a-zA-Z\s]", "", clean)
    words = [w for w in clean.split() if w]
    
    if len(words) < 3 or len(words) > 7:
        return False
        
    bad_endings = {"the", "a", "an", "and", "or", "if", "two", "given", "input", "inputs", "provided", "of", "in"}
    if words[-1].lower() in bad_endings:
        return False
        
    return True


def _extract_titles(text: str):
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    titles = []
    for line in lines:
        clean = line
        # Usuń punktory (np. "-", "*")
        if clean.startswith("-") or clean.startswith("*"):
            clean = clean[1:].strip()
            
        clean = re.sub(r"^\d+[\.)]\s*", "", clean)
        
        clean = clean.strip(".,;:!'\"")
        titles.append(clean)
        
    return titles


def load_or_generate_topics(num_topics=100, force=False, max_attempts=200):
    existing = []
    if os.path.exists(TOPICS_FILE) and not force:
        try:
            df = pd.read_csv(TOPICS_FILE)
            existing = [str(x).strip() for x in df["topic"].tolist() if str(x).strip()]
        except Exception:
            existing = []

    titles = []
    seen = set(_normalize_title(t) for t in existing)
    
    for t in existing:
        if _valid_title(t):
            titles.append(t)

    BATCH_SIZE = 15
    attempts = 0
    no_new_attempts = 0
    
    while len(titles) < num_topics and attempts < max_attempts:
        remaining = num_topics - len(titles)
        to_request = min(BATCH_SIZE, remaining)
        
        attempts += 1
        temperature = TOPICS_TEMPERATURES[attempts % len(TOPICS_TEMPERATURES)]
        category = random.choice(TOPICS_CATEGORIES)

        print(f"Attempt {attempts}: need {remaining} topics, temp={temperature:.2f}, cat='{category}'", flush=True)

        existing_snippet = "\n".join(f"- {t}" for t in titles[-10:])
        prompt = TOPICS_PROMPT_TEMPLATE.format(count=to_request, category=category)

        if no_new_attempts >= 3:
            fallback_category = random.choice([c for c in TOPICS_CATEGORIES if c != category])
            print(f" -> Model stuck. Forcing context shift to '{fallback_category}'...", flush=True)
            prompt = (
                f"Generate 5 completely UNUSUAL and highly creative Python programming task titles.\n"
                f"CATEGORY: {fallback_category}.\n"
                "Do NOT use common examples. Do NOT generate anything similar to these:\n"
                f"{existing_snippet}\n\n"
                "RULES: 3-7 words, NO numbers, NO bullet points. One title per line."
            )

        text = ollama_generate(prompt, temperature)
        if not text:
            print(" -> Empty response, retrying...", flush=True)
            no_new_attempts += 1
            continue

        new_items = _extract_titles(text)
        if not new_items:
            print(" -> No titles found in response, retrying...", flush=True)
            no_new_attempts += 1
            continue

        new_count = 0
        for it in new_items:
            if not _valid_title(it):
                continue
            key = _normalize_title(it)
            if key in seen:
                continue
                
            seen.add(key)
            titles.append(it)
            new_count += 1
            print('.', end='', flush=True)
            
            if len(titles) >= num_topics:
                break

        if new_count == 0:
            print("\n -> No new valid/unique topics extracted.", flush=True)
            no_new_attempts += 1
        else:
            print(f"\n -> Added {new_count} new topics.", flush=True)
            no_new_attempts = 0

    if len(titles) < num_topics:
        print(f"Warning: only generated {len(titles)} topics out of requested {num_topics} after {attempts} attempts.")

    df_out = pd.DataFrame({
        "topic_id": range(len(titles)),
        "topic": titles[:num_topics]
    })
    df_out.to_csv(TOPICS_FILE, index=False)
    return df_out
