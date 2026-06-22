def sort_words(word_list):
    if not all(isinstance(item, str) for item in word_list):
        raise ValueError("All items in the list must be strings")
    return sorted(word_list)

if __name__ == '__main__':
    sample_list = ["banana", "apple", "cherry", "date", "elderberry"]
    print(sort_words(sample_list))