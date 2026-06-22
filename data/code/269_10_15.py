import string

def isolate_punctuation(text):
    punctuation_table = str.maketrans('', '', ''.join(string.punctuation))
    cleaned_text = text.translate(punctuation_table)
    return [char for char in text if char not in cleaned_text]

if __name__ == '__main__':
    sample_text = "Hello, world! How are you?"
    print(isolate_punctuation(sample_text))