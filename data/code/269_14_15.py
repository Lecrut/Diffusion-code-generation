def extract_and_sort_punctuation(text):
    punctuation_chars = set(".,?!:;\'\"()[]{}")
    extracted_punctuations = [char for char in text.lower() if char in punctuation_chars]
    return sorted(list(set(extracted_punctuations)))

if __name__ == '__main__':
    sample_string = "Hello, world! How are you? This is a test."
    result = extract_and_sort_punctuation(sample_string)
    print(result)