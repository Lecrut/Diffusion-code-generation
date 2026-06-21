def sort_words_by_length(words):
    return sorted(words, key=len)

if __name__ == '__main__':
    sample_words = ["apple", "banana", "cherry", "date"]
    sorted_words = sort_words_by_length(sample_words)
    print(sorted_words)