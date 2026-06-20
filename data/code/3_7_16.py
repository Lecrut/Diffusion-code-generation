VOWEL_SET = frozenset('aeiouAEIOU')

def _is_vowel(char: str) -> bool:
    return char in VOWEL_SET

def remove_vowels(text: str) -> str:
    if not text:
        return ""
    return ''.join(char for char in text if not _is_vowel(char))

if __name__ == '__main__':
    test_cases = ["Beautiful Day", "Programming is Fun", "AI and ML"]
    for case in test_cases:
        cleaned = remove_vowels(case)
        print(cleaned)