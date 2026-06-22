import re

def isolate_punctuation(text):
    return re.findall(r'[^\w\s]', text)

if __name__ == '__main__':
    sample_text = "Hello, world! This is a test."
    print(isolate_punctuation(sample_text))