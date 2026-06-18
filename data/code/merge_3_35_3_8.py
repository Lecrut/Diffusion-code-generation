def count_vowels(text: str) -> int:
    return sum(1 for char in text.lower() if char in 'aeiou')

if __name__ == '__main__':
    sample_strings = ["Hello World", "AEIOU", "Python3.9"]
    for s in sample_strings:
        print(f"Vowels in '{s}': {count_vowels(s)}")