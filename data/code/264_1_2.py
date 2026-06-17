import re
def extract_words(text):
    words = set(word for word in re.findall(r'[a-zA-Z0-9]+', text))
    return words
if __name__ == '__main__':
    sample_string = "Hello world! This is a test string with numbers 123 and symbols @#$."
    result = extract_words(sample_string)
    print(result)