def count_vowels(text: str) -> int:
    return sum(1 for c in text if c.lower() in "aeiou")

if __name__ == '__main__':
    samples = ["Hello", "AEIOU", "rhythm"]
    results = [count_vowels(s) for s in samples]
    print(f"Vowel counts: {dict(zip(samples, results))}")