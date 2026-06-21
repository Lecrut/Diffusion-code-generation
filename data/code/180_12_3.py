def is_word_in_list(word, word_list):
    lowercased_words = set(w.lower() for w in word_list)
    return word.lower() in lowercased_words

if __name__ == '__main__':
    sample_word = 'Java'
    sample_list = ['java', 'c++', 'Python', 'ruby']
    print(is_word_in_list(sample_word, sample_list))