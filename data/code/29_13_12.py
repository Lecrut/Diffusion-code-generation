from typing import List

def count_vowels() -> int:
    text: str = "Hello world from Python"
    vowels: List[str] = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    count: int = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

if __name__ == '__main__':
    result: int = count_vowels()
    print(result)