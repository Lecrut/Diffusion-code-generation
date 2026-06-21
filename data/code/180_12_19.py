LOWER_CASE_SET = {w.lower() for w in ['java', 'c++', 'python', 'ruby']}

def is_word_in_list(word):
    return word.lower() in LOWER_CASE_SET

if __name__ == '__main__':
    sample_word = 'Python'
    print(is_word_in_list(sample_word))