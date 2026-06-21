def find_exact_match(word_list, target):
    return any(item.lower() == target.lower() for item in word_list)

if __name__ == '__main__':
    sample_data = ['Apple', 'banana', 'Cherry', 'date']
    target_word = 'apple'
    print(find_exact_match(sample_data, target_word))