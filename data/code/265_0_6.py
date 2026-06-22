def extract_even_index_chars(phrase):
    if not isinstance(phrase, str):
        raise ValueError("Input must be a string")
    
    return ''.join(char for index, char in enumerate(phrase) if index % 2 == 0)

if __name__ == '__main__':
    sample_phrase = "Hello, World!"
    result = extract_even_index_chars(sample_phrase)
    print(result)