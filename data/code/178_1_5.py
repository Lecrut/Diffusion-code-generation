import re
def extract_words(text):
    return re.findall(r'[a-zA-Z]+', text)
if __name__ == '__main__':
    sample_string1 = "Hello world! This is a test sentence with various spaces."
    sample_string2 = "  Multiple   spaces   and   punctuation , and numbers 123. "
    sample_string3 = "Python programming is fun"
    print(extract_words(sample_string1))
    print(extract_words(sample_string2))
    print(extract_words(sample_string3))