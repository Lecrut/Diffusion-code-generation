def remove_vowels(input_string):
    VOWEL_MAP = {
        'a': 'a', 'e': 'e', 'i': 'i', 'o': 'o', 'u': 'u',
        'A': 'A', 'E': 'E', 'I': 'I', 'O': 'O', 'U': 'U'
    }
    def is_not_vowel(char):
        return char not in VOWEL_MAP
    filtered_chars = filter(is_not_vowel, input_string)
    return "".join(filtered_chars)

if __name__ == '__main__':
    test_input = "Data Science"
    output = remove_vowels(test_input)
    print(output)