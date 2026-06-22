def replace_punctuation(text):
    punctuation_map = str.maketrans('', '', '.,!?;:')
    return text.translate(punctuation_map)

if __name__ == '__main__':
    sample_string = "Hello, world! How are you? This is a test."
    result = replace_punctuation(sample_string)
    print(result)