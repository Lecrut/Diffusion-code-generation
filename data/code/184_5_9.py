def case_insensitive_match(word, word_list):
    lower_word = word.lower()
    for w in word_list:
        if w.lower() == lower_word:
            return True
    return False

if __name__ == '__main__':
    sample_word = 'Python'
    sample_list = ['java', 'C++', 'python', 'ruby']
    print(case_insensitive_match(sample_word, sample_list))