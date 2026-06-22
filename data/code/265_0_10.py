def extract_even_index_chars(phrase):
    def is_valid_char(char):
        return char.isalnum()

    filtered_phrase = ''.join(filter(is_valid_char, phrase))
    return ''.join(char for index, char in enumerate(filtered_phrase) if index % 2 == 0)

if __name__ == '__main__':
    sample_phrase = "Hello, World! 123"
    result = extract_even_index_chars(sample_phrase)
    print(result)