import re
def extract_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return words
if __name__ == '__main__':
    sample_string = "Hello world! This is a test, how are you doing today?"
    result = extract_words(sample_string)
    print(result)