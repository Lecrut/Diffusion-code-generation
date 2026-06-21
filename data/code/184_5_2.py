def case_insensitive_match(word_list, target):
    return any(w.lower() == target.lower() for w in word_list)

if __name__ == '__main__':
    sample_data = ['Apple', 'banana', 'Cherry', 'date']
    target_word = 'apple'
    print(case_insensitive_match(sample_data, target_word))