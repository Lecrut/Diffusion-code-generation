import string

def replace_punctuation_with_spaces(text):
    return text.translate(str.maketrans('', '', string.punctuation))

if __name__ == '__main__':
    sample_text = "Hello, world! How's it going?"
    print(replace_punctuation_with_spaces(sample_text))