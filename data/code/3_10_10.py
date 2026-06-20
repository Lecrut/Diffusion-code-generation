def remove_vowels(text: str) -> str:
    vowels = 'aeiouAEIOU'
    trans_table = str.maketrans('', '', vowels)
    return text.translate(trans_table)

if __name__ == '__main__':
    sample_input = 'The quick brown fox jumps over the lazy dog'
    output = remove_vowels(sample_input)
    print(output)
    sample_input_2 = 'Python is AWESOME for coding'
    output_2 = remove_vowels(sample_input_2)
    print(output_2)
    sample_input_3 = 'aeiou AEIOU'
    output_3 = remove_vowels(sample_input_3)
    print(output_3)