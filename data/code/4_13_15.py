def _validate_input(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return len(text) > 0

def count_consonants(text):
    if not _validate_input(text):
        return 0
    vowels = {'a', 'e', 'i', 'o', 'u'}
    consonant_set = set()
    for char in text:
        if char.isalpha():
            lower_char = char.lower()
            if lower_char not in vowels:
                consonant_set.add(char)
    return len([char for char in text if char.isalpha() and char.lower() not in vowels])

if __name__ == '__main__':
    sample_input = "Rhythm & Blues 123"
    final_result = count_consonants(sample_input)
    print(final_result)