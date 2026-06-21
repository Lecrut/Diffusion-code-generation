import re

def tokenize_string(sentence):
    if not isinstance(sentence, str):
        raise ValueError("Input must be a string")
    
    cleaned_sentence = re.sub(r'[^a-zA-Z\s]', '', sentence)
    words = cleaned_sentence.split()
    return list(dict.fromkeys(words))

if __name__ == '__main__':
    sample_sentence = "Hello World! This is a test sentence with numbers 123."
    result = tokenize_string(sample_sentence)
    print(result)