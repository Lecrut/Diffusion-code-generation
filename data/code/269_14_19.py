def extract_and_sort_punctuation(text):
    punctuation_marks = {'.', ',', '!', '?', ':', ';'}
    extracted_punctuation = [char for char in text.lower() if char in punctuation_marks]
    return ''.join(sorted(set(extracted_punctuation)))

if __name__ == '__main__':
    sample_string = "Hello, world! How are you? This is a test."
    result = extract_and_sort_punctuation(sample_string)
    print(result)