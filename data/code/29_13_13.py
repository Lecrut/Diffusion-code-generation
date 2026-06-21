from typing import Final

VOWEL_SET: Final[set] = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

def _is_valid_text(text: str) -> bool:
    return isinstance(text, str)

def count_vowels(text: str) -> int:
    if not _is_valid_text(text):
        return 0
    return sum(1 for char in text if char in VOWEL_SET)

if __name__ == '__main__':
    static_phrase = "AeIoU XxYyZz 123"
    result = count_vowels(static_phrase)
    print(result)