import string

def isolate_punctuation(input_string):
    punctuation = set(string.punctuation)
    result = []
    for char in input_string:
        if char in punctuation:
            result.append(char)
        else:
            result.append(' ')
    return ''.join(result)

if __name__ == '__main__':
    sample_input = "Hello, world! How are you?"
    print(isolate_punctuation(sample_input))