import re

def find_words(text):
    words = re.split(r'\W+', text)
    return [word for word in words if word]

if __name__ == '__main__':
    sample_text = "Hello, world! This is a test string with multiple   spaces and punctuation."
    words = find_words(sample_text)
    print(words)