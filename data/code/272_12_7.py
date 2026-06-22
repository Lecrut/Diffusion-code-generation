def sort_words(word_list):
    if not all(isinstance(word, str) for word in word_list):
        raise ValueError("All elements in the list must be strings.")
    return sorted(word_list)

if __name__ == '__main__':
    sample_words = ["banana", "apple", "cherry"]
    try:
        sorted_words = sort_words(sample_words)
        print(sorted_words)
    except ValueError as e:
        print(e)