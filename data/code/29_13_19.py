from typing import Set

def count_vowels(text: str) -> int:
    vowels: Set[str] = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    return sum(1 for char in text if char in vowels)

if __name__ == '__main__':
    text: str = "Hello World"
    result: int = count_vowels(text)
    print(result)