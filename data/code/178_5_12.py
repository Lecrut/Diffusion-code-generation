def extract_words(text):
    import re
    words = re.findall(r'\b\w+\b', text.lower())
    return words

if __name__ == '__main__':
    sample_string = "Hello, world! This is a test string with some punctuation and numbers 123."
    result = extract_words(sample_string)
    print(result)