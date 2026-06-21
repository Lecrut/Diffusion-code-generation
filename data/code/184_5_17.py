def find_exact_match(word_list, search_word):
    return any(word.lower() == search_word.lower() for word in word_list)

if __name__ == '__main__':
    sample_data = ["Apple", "banana", "Cherry", "date"]
    search_term = "apple"
    print(find_exact_match(sample_data, search_term))