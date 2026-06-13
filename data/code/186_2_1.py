def sort_words_case_insensitive(word_list):
    return sorted(word_list, key=str.lower)
if __name__ == '__main__':
    sample_list = ["Apple", "banana", "Cherry", "date", "apricot"]
    sorted_list = sort_words_case_insensitive(sample_list)
    print(sorted_list)