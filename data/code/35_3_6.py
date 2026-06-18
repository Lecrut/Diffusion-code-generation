def count_vowels(text: str) -> int:
    return sum(c.lower() in "aeiou" for c in text)

if __name__ == '__main__':
    sample_strings = ["Hello, World!", "AEIOU", "", "Python3"]
    results = [count_vowels(s) for s in sample_strings]
    print("Vowel counts:", list(zip(sample_strings, results)))