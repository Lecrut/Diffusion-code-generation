def case_insensitive_match(word, word_list):
    return any(w.lower() == word.lower() for w in word_list)

if __name__ == '__main__':
    sample_word = 'Python'
    sample_list = ['java', 'C++', 'python', 'ruby']
    print(case_insensitive_match(sample_word, sample_list))