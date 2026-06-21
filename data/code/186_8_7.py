def sort_words_by_length(word_list):
    return sorted(word_list, key=len)

if __name__ == '__main__':
    SAMPLE_WORDS = ["apple", "banana", "kiwi", "orange", "grapefruit"]
    sorted_list = sort_words_by_length(SAMPLE_WORDS)
    print(sorted_list)