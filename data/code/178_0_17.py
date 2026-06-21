def split_into_words(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    words = text.split()
    return [word.strip() for word in words]

if __name__ == '__main__':
    sample_string = "  Hello   world! This is a test, how are you doing today?  "
    result = split_into_words(sample_string)
    print(result)