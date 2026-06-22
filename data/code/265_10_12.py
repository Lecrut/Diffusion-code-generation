def extract_unique_chars(phrase):
    if not isinstance(phrase, str):
        raise ValueError("Input must be a string")
    
    unique_chars = set(phrase)
    sorted_chars = ''.join(sorted(unique_chars))
    return sorted_chars

if __name__ == '__main__':
    sample_phrase = "hello world"
    result = extract_unique_chars(sample_phrase)
    print(result)