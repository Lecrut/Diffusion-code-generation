import re

def count_consonants(word):
    cleaned_word = re.sub(r'[^a-zA-Z]', '', word)
    consonants = re.findall(r'[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]', cleaned_word)
    return len(consonants)

if __name__ == '__main__':
    sample_word = "Hello, World! 123"
    result = count_consonants(sample_word)
    print(result)