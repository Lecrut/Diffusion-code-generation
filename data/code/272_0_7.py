def sort_words(word_list):
    if not isinstance(word_list, list) or not all(isinstance(w, str) for w in word_list):
        raise ValueError("Input must be a list of strings")
    return sorted(word_list)

if __name__ == '__main__':
    sample_words = ["banana", "apple", "cherry", "date", "elderberry"]
    sorted_list = sort_words(sample_words)
    print(*sorted_list)