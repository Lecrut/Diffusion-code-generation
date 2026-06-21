import re

def is_word_in_dict(word, dictionary):
    word = re.sub('[^\\w]', '', word).lower()
    return word in dictionary
if __name__ == '__main__':
    sample_dict = {'apple': 1, 'banana': 2, 'cherry': 3}
    print(is_word_in_dict('Banana!', sample_dict))
    print(is_word_in_dict('orange', sample_dict))