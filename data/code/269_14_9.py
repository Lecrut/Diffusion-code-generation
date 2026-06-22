import string

def isolate_punctuation(s):
    punctuation = set(string.punctuation)
    result = sorted([char for char in s if char in punctuation])
    return ''.join(result)

if __name__ == '__main__':
    sample_string = "Hello, World! This is a test."
    print(isolate_punctuation(sample_string))