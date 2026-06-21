def case_insensitive_match(word_list, target):
    return any(w.lower() == target.lower() for w in word_list)

if __name__ == '__main__':
    sample_words = ['Apple', 'banana', 'Cherry', 'date']
    search_term = 'apple'
    print(case_insensitive_match(sample_words, search_term))