import re
def split_words(text):
    return re.findall(r'\b\w+\b', text)
if __name__ == '__main__':
    sample_text = "Hello, world! This is a test string with punctuation."
    result = split_words(sample_text)
    print(result)