def sort_words(word_list):
    return sorted(word_list)

if __name__ == '__main__':
    sample_words = ["orange", "grape", "kiwi", "pineapple", "mango"]
    sorted_list = sort_words(sample_words)
    for word in sorted_list:
        print(word)