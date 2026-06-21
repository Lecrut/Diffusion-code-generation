def extract_words(text):
    import re
    words = text.split()
    cleaned_words = [re.sub(r'\W+', '', word).lower() for word in words if re.sub(r'\W+', '', word)]
    return cleaned_words

if __name__ == '__main__':
    sample_string = "Hello, world! This is a test string with some - punctuation and numbers 123."
    result = extract_words(sample_string)
    print(result)