def word_exists(word_list, target_word):
    word_set = set(word_list)
    return target_word in word_set

if __name__ == '__main__':
    sample_data = ["apple", "banana", "cherry", "date"]
    target = "banana"
    print(word_exists(sample_data, target))