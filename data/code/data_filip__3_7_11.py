def _is_vowel(char: str) -> bool:
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    return char in vowels

def remove_vowels(text: str) -> str:
    if not text:
        return ""
    return ''.join([char for char in text if not _is_vowel(char)])

if __name__ == '__main__':
    test_cases = [
        "Programming is fun",
        "AEIOUaeiou",
        "sky",
        ""
    ]
    for case in test_cases:
        print(remove_vowels(case))