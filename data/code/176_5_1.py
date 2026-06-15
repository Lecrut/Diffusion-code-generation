import re
def extract_alphabetic_words(text):
    words = re.findall(r'[a-zA-Z]+', text)
    return words
if __name__ == '__main__':
    sample_string = "Hello world! This is a test, with 123 numbers and symbols like @#$."
    result = extract_alphabetic_words(sample_string)
    print(result)