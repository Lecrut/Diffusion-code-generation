def count_vowels(s: str) -> int:
    return sum(1 for c in s.lower() if c in "aeiou")

if __name__ == "__main__":
    test_strings = ["Hello World", "AEIOU", "", "Pythonic"]
    results = [count_vowels(text) for text in test_strings]
    print("\n".join(f"{text!r}: {v}" for v, text in zip(results, test_strings)))