import string

def isolate_punctuation(text):
    punctuation = set(string.punctuation)
    isolated = [char for char in text.lower() if char in punctuation]
    return ''.join(sorted(set(isolated)))

if __name__ == '__main__':
    sample_text = "Hello, World! This is a Test."
    print(isolate_punctuation(sample_text))