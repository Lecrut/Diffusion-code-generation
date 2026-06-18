import string

def count_vowels(text: str) -> int:
    return sum(1 for char in text.lower() if char in set('aeiou'))

if __name__ == '__main__':
    samples = ["Hello World", "AEIOU aeiou", "", "Python 3.9"]
    [print(f"Vowels in '{s}': {count_vowels(s)}") for s in samples]