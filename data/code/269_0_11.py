import string

def is_punctuation(char):
    return char in string.punctuation

def isolate_punctuation(text):
    result = []
    for char in text:
        if is_punctuation(char):
            result.append(f'{char} ')
        else:
            result.append(char)
    return ''.join(result)

if __name__ == '__main__':
    sample_text = "Hello, world! How are you?"
    print(isolate_punctuation(sample_text))