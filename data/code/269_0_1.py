import re

def isolate_punctuation(text):
    return re.sub(r'([^\w\s])', r'\1 ', text)

if __name__ == '__main__':
    sample_text = "Hello, world! How are you?"
    print(isolate_punctuation(sample_text))