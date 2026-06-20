VOWEL_SET = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
CHAR_ROLE = {v: 'vowel' for v in VOWEL_SET}

def remove_vowels(text):
    return ''.join([char for char in text if char not in CHAR_ROLE])

if __name__ == '__main__':
    sample_input = "The quick brown fox jumps over the lazy dog"
    output_result = remove_vowels(sample_input)
    print(output_result)