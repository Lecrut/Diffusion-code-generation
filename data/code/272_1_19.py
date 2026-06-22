def sort_words(word_list):
    if not isinstance(word_list, list) or not all(isinstance(w, str) for w in word_list):
        raise ValueError("Input must be a list of strings")
    return sorted(word_list)

if __name__ == '__main__':
    sample_list = ["banana", "apple", "cherry", "date"]
    sorted_result = sort_words(sample_list)
    print(sorted_result)