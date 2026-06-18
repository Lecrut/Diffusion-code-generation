def count_vowels(text: str) -> int:
    return sum(1 for c in text.lower() if c in "aeiou")

if __name__ == '__main__':
    samples = ["Hello World", "AEIOU aeiou", "", "Pythonic code"]
    for sample in samples:
        print(f"{sample!r}: {count_vowels(sample)}")