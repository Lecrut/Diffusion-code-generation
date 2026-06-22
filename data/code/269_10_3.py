import string

def isolate_punctuation(s):
    return [char for char in s if char in string.punctuation]

if __name__ == '__main__':
    sample_string = "Hello, world! How are you?"
    print(isolate_punctuation(sample_string))