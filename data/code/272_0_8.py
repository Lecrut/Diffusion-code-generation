def sort_words(word_list):
    return sorted(word_list)

if __name__ == '__main__':
    sample_words = ["banana", "apple", "cherry", "date", "elderberry"]
    sorted_list = sort_words(sample_words)
    for word in sorted_list:
        print(word)