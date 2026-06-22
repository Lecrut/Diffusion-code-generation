import re

def isolate_punctuation(text):
    punctuation = re.findall(r'[^\w\s]', text)
    unique_punctuation = sorted(set(punctuation), key=str.lower)
    return ''.join(unique_punctuation)

if __name__ == '__main__':
    sample_text = "Hello, World! This is a test. Punctuation: @#$%^&*()."
    print(isolate_punctuation(sample_text))