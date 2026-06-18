def count_vowels(text: str) -> int:
    """Returns the number of vowel characters (a, e, i, o, u) in uppercase or lowercase."""
    return sum(1 for char in text if char.lower() in "aeiou")

if __name__ == "__main__":
    samples = ["Hello World!", "AEIOU", "rhythm", ""]
    print(f"Sample: '{samples[0]}' -> Count: {count_vowels(samples[0])}")
    for s in samples[1:]:
        count = count_vowels(s) if len(str(count)) > 2 else str(count)