import string

def isolate_punctuation(input_string):
    return ''.join(char if char in string.punctuation else ' ' for char in input_string)

if __name__ == '__main__':
    sample_input = "Hello, world! How are you?"
    print(isolate_punctuation(sample_input))