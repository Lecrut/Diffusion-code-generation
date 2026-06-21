import re

def is_word_in_dictionary(word, dictionary):
    word = re.sub('[^\\w]', '', word).lower()
    return word in dictionary
if __name__ == '__main__':
    sample_dict = {'apple': 1, 'banana': 2, 'cherry': 3}
    print(is_word_in_dictionary('Banana!', sample_dict))
    print(is_word_in_dictionary('orange', sample_dict))