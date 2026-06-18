def count_vowels(text: str) -> int:
    return sum(1 for c in text.lower() if c in 'aeiou')

if __name__ == '__main__':
    samples = ["Hello World", "AEIOU aeiou", "", "Pythonic"]
    for s in samples:
        print(f"String '{s}' -> {count_vowels(s)} vowels")