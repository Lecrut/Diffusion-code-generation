from typing import Dict, List, Tuple

def count_vowels(text: str) -> Dict[str, int]:
    vowels = set("aeiouAEIOU")
    counts: Dict[str, int] = {char: 0 for char in "aeiou"}
    for char in text:
        if char in vowels:
            lower_char = char.lower()
            counts[lower_char] += 1
    return counts

if __name__ == '__main__':
    sample_text = "Hello World, this is a deterministic example."
    result = count_vowels(sample_text)
    print(result)