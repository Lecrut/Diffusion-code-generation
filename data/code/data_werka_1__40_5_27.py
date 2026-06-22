import re

def extract_first_letters(text):
    word_pattern = re.compile('\\b[a-zA-Z]+\\b')
    words = word_pattern.findall(text)
    first_letters_dict = {word: word[0] for word in words}
    return first_letters_dict
if __name__ == '__main__':
    sample_text = 'Hello, world! This is a test sentence with punctuation.'
    result = extract_first_letters(sample_text)
    print(result)