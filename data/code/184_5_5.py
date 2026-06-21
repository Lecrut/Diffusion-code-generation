def case_insensitive_match(word_list, target_word):
    return any(word.lower() == target_word.lower() for word in word_list)

if __name__ == '__main__':
    sample_data = ['Apple', 'banana', 'Cherry', 'date']
    target = 'apple'
    print(case_insensitive_match(sample_data, target))