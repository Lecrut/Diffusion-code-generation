import re

def is_word_in_dict(word, dictionary):
    word = re.sub(r'[^\w]', '', word).lower()
    return word in dictionary

if __name__ == '__main__':
    sample_word = "Hello"
    sample_dict = {"hello": True, "world": False}
    print(is_word_in_dict(sample_word, sample_dict))