VOWEL_SET = frozenset("aeiouAEIOU")

def validate_input(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return True

def count_vowels(text):
    validate_input(text)
    unique_chars = set(text)
    found = unique_chars.intersection(VOWEL_SET)
    total_count = 0
    for char in found:
        total_count += text.count(char)
    return total_count

if __name__ == '__main__':
    sample_text = "Programming is awesome"
    result = count_vowels(sample_text)
    print(result)