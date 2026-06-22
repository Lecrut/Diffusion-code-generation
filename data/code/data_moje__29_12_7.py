_VOWELS = frozenset("aeiouAEIOU")

def _is_valid_input(data):
    return isinstance(data, str)

def count_vowels(text):
    if not _is_valid_input(text):
        raise TypeError("Input must be a string")
    return sum(1 for char in text if char in _VOWELS)

if __name__ == '__main__':
    sample_text = "The quick brown fox jumps over the lazy dog"
    print(count_vowels(sample_text))