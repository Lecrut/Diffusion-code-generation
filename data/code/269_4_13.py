import string

def replace_punctuation_with_spaces(text):
    punctuation_to_space = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
    return text.translate(punctuation_to_space)

if __name__ == '__main__':
    sample_string = "Hello world! How are you, today? Let's check: 123."
    result = replace_punctuation_with_spaces(sample_string)
    print(result)