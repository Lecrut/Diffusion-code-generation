LOWER_WORDS = set()

def initialize_word_list(word_list):
    global LOWER_WORDS
    LOWER_WORDS = {word.lower() for word in word_list}

def is_word_in_list(word):
    return word.lower() in LOWER_WORDS

if __name__ == '__main__':
    sample_word = 'Python'
    sample_list = ['java', 'c++', 'python', 'ruby']
    initialize_word_list(sample_list)
    print(is_word_in_list(sample_word))