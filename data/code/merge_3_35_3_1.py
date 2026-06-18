def count_vowels(text: str) -> int:
    return sum(1 for char in text.lower() if char in 'aeiou')

if __name__ == '__main__':
    sample_strings = ["Hello, World!", "AEIOU", "rhythm"]
    [print(f"'{s}': {count_vowels(s)}") for s in sample_strings]