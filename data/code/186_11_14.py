def sort_words_desc(words):
    return sorted(words, reverse=True)

if __name__ == '__main__':
    sample_words = ["apple", "zebra", "banana", "cat", "dog"]
    sorted_list = sort_words_desc(sample_words)
    print(sorted_list)