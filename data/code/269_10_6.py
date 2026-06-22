import string

def isolate_punctuation(text):
    punctuation_set = set(string.punctuation)
    return [char for char in text if char in punctuation_set]

if __name__ == '__main__':
    sample_text = "Python, Java! C++ & JavaScript?"
    print(isolate_punctuation(sample_text))