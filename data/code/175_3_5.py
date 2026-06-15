import re
def separate_words(text):
    words = re.findall(r'\b\w+\b', text)
    return words
if __name__ == '__main__':
    sample_string = "Hello world! This is a test, with various spaces and punctuation."
    result = separate_words(sample_string)
    print(result)