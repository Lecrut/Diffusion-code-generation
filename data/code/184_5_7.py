def case_insensitive_match(word, word_list):
    lower_word = word.lower()
    return any(w.lower() == lower_word for w in word_list)

if __name__ == '__main__':
    sample_word = 'Python'
    sample_list = ['java', 'C++', 'python', 'ruby']
    print(case_insensitive_match(sample_word, sample_list))