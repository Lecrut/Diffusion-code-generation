import re

def is_word_in_dict(word, dictionary):
    word = re.sub('[^\\w]', '', word).lower()
    return word in dictionary
if __name__ == '__main__':
    sample_dictionary = {'apple': 1, 'banana': 2, 'cherry': 3}
    print(is_word_in_dict('Apple', sample_dictionary))
    print(is_word_in_dict('Banana!', sample_dictionary))
    print(is_word_in_dict('orange', sample_dictionary))