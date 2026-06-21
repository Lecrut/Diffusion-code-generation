VOWEL_CHARS = frozenset("aeiouAEIOU")

def _validate_text(data: str) -> None:
    if not isinstance(data, str):
        raise TypeError(f"Expected string, got {type(data).__name__}")

def count_vowels(text: str) -> int:
    _validate_text(text)
    count = 0
    for char in text:
        if char in VOWEL_CHARS:
            count += 1
    return count

if __name__ == '__main__':
    sample_sentence = "Programming is an art form"
    result = count_vowels(sample_sentence)
    print(result)