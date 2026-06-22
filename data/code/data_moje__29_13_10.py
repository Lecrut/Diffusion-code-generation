from typing import Dict, Any

def count_vowels(text: str) -> Dict[str, Any]:
    vowels = "aeiouAEIOU"
    counts = {char: 0 for char in "aeiou"}
    total = 0
    for char in text:
        if char in vowels:
            counts[char.lower()] += 1
            total += 1
    return {"counts": counts, "total": total}

if __name__ == "__main__":
    sample_text = "Hello World, this is a deterministic example."
    result = count_vowels(sample_text)
    print(result["total"])
    print(result["counts"])