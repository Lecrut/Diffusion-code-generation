def _validate_text(text):
    return isinstance(text, str)

def count_consonants(text):
    if not _validate_text(text):
        raise TypeError("Input must be a string")
    vowels = set("aeiouAEIOU")
    consonant_chars = [char for char in text if char.isalpha() and char not in vowels]
    return len(consonant_chars)

if __name__ == '__main__':
    sample_input = "Python 3.9 is great! @#%"
    calculated_count = count_consonants(sample_input)
    print(calculated_count)