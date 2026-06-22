def sort_words(word_list):
    return sorted(word_list)

if __name__ == '__main__':
    SAMPLE_WORDS = ["banana", "apple", "cherry", "date", "elderberry"]
    sorted_result = sort_words(SAMPLE_WORDS)
    print(sorted_result)