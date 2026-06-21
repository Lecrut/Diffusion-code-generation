def case_insensitive_match(word_list, target_word):
    return any((w.lower() == target_word.lower() for w in word_list))
if __name__ == '__main__':
    sample_words = ['Apple', 'banana', 'Cherry', 'date']
    target = 'apple'
    print(case_insensitive_match(sample_words, target))