def count_vowels(text: str) -> int:
    vowels = {"a", "e", "i", "o", "u"}
    unique_chars = set(text.lower())
    return len(unique_chars & vowels)

if __name__ == "__main__":
    sample_text = "Hello World"
    result = count_vowels(sample_text)
    print(result)