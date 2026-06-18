def count_vowels(s: str) -> int:
    return sum(1 for c in s.lower() if c in 'aeiou')

if __name__ == '__main__':
    test_strings = ["Hello World!", "AEIOU aeiou", "Rhythm"]
    [print(f"{s!r} has {count_vowels(s)} vowels") for s in test_strings]