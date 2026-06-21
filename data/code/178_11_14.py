import re

def isolate_words(phrase):
    return [word for word in re.findall(r'\b\w+\b', phrase)]

if __name__ == '__main__':
    sample_phrase = "Hello, world! This is a test phrase with 123 numbers and punctuation."
    print(isolate_words(sample_phrase))