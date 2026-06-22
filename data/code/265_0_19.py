def is_even_index(index):
    return index % 2 == 0

def extract_even_index_chars(phrase):
    if not isinstance(phrase, str):
        raise ValueError("Input must be a string")
    
    result = ''.join(char for index, char in enumerate(phrase) if is_even_index(index))
    return result

if __name__ == '__main__':
    sample_phrase = "Hello, World!"
    print(extract_even_index_chars(sample_phrase))