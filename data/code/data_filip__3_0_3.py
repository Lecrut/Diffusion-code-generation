def remove_vowels(s: str) -> str:
    return "".join(c for c in s if c.lower() not in "aeiou")

if __name__ == "__main__":
    samples = ["Hello", "World", "Python", "AEIOU", "aeiou", "Rhythm", ""]
    for sample in samples:
        print(remove_vowels(sample))