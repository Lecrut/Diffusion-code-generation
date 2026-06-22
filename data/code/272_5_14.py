def sort_words_reverse_alphabetically(word_list):
    sorted_words = sorted(word_list, reverse=True)
    return sorted_words

if __name__ == '__main__':
    sample_words = ["zebra", "yak", "xray", "whale", "vulture"]
    result = sort_words_reverse_alphabetically(sample_words)
    print(result)