def count_vowels(s: str) -> int:
    return sum(c.lower() in "aeiou" for c in s)

if __name__ == '__main__':
    test_strings = ["Hello", "AEIOU", "", "Python3ic"]
    [print(f"'{s}' has {count_vowels(s)} vowels") for s in test_strings]