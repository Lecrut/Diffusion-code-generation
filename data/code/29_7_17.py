def _is_vowel(char):
    return char in 'aeiouAEIOU'

def count_vowels(s):
    if not s:
        return 0
    total = 0
    for char in s:
        if _is_vowel(char):
            total += 1
    return total

if __name__ == '__main__':
    test_cases = [
        "PyThOn",
        "HELLO",
        "sky",
        "aeiou",
        "AEIOU",
        "rhythm",
        "The quick brown fox jumps over the lazy dog"
    ]
    for text in test_cases:
        print(f"{text}: {count_vowels(text)}")