import string

def isolate_punctuation(text):
    punctuation_table = str.maketrans('', '', ''.join(string.ascii_letters + string.digits))
    cleaned_text = text.translate(punctuation_table)
    return [char for char in cleaned_text if char in string.punctuation]

if __name__ == '__main__':
    sample_text = "Hello, world! How are you?"
    print(isolate_punctuation(sample_text))