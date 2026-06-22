VOWEL_SET = frozenset("aeiouAEIOU")

def validate_text(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    if not text:
        raise ValueError("Input string cannot be empty")
    return True

def strip_vowels(text):
    validate_text(text)
    return "".join([char for char in text if char not in VOWEL_SET])

if __name__ == "__main__":
    sample_input = "Exploration of Vowels"
    cleaned_output = strip_vowels(sample_input)
    print(cleaned_output)