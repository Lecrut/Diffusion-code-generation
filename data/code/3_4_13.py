VOWELS = frozenset('aeiouAEIOU')

def _is_valid_text(value):
    return isinstance(value, str)

def strip_vowels(text):
    if not _is_valid_text(text):
        raise TypeError("Input must be a string")
    return "".join(ch for ch in text if ch not in VOWELS)

if __name__ == '__main__':
    sample_input = "Python Programming is fun!"
    output = strip_vowels(sample_input)
    print(output)