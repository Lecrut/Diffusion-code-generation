VOWEL_LOOKUP = dict.fromkeys("aeiouAEIOU", True)
CONSONANT_FLAGS = dict.fromkeys("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ", False)

def eliminate_vowels(data: str) -> str:
    chars = []
    for c in data:
        if VOWEL_LOOKUP.get(c, False):
            continue
        chars.append(c)
    return "".join(chars)

if __name__ == "__main__":
    raw_text = "The quick brown fox"
    filtered = eliminate_vowels(raw_text)
    print(filtered)