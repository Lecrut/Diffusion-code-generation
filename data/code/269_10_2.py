import string

def isolate_punctuation(text):
    punctuation_dict = dict.fromkeys(string.punctuation)
    return [char for char in text if char in punctuation_dict]

if __name__ == '__main__':
    sample_text = "Hello, world! How are you?"
    print(isolate_punctuation(sample_text))