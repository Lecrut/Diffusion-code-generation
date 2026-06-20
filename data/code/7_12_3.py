import string

def has_punctuation_or_symbols(text):
    punctuation_set = set(string.punctuation)
    for char in text:
        if char in punctuation_set:
            return True
    return False
if __name__ == '__main__':
    sample_strings = ['Hello World', 'Hello, World!', 'Python3.10', 'No punctuation here', 'Special chars: @#$%', '']
    for s in sample_strings:
        result = has_punctuation_or_symbols(s)
        print(result)