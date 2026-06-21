from typing import Final

TEXT: Final[str] = "Hello World. This is a sample text with vowels."

VOWELS: Final[str] = "aeiouAEIOU"

def count_vowels(text: str) -> int:
    count = 0
    for char in text:
        if char in VOWELS:
            count += 1
    return count

if __name__ == '__main__':
    result = count_vowels(TEXT)
    print(result)