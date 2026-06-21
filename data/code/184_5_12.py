def case_insensitive_match(word_list, target):
    return any(w.lower() == target.lower() for w in word_list)

if __name__ == '__main__':
    sample_data = ['apple', 'Banana', 'cherry', 'date']
    target_word = 'banana'
    print(case_insensitive_match(sample_data, target_word))