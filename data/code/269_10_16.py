import string

def isolate_punctuation(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    punctuation_set = set(string.punctuation)
    return [char for char in text if char in punctuation_set]

if __name__ == '__main__':
    sample_text = "Hello, world! How are you?"
    print(isolate_punctuation(sample_text))