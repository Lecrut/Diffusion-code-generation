def sort_words(word_list):
    if not all(isinstance(item, str) for item in word_list):
        raise ValueError("All elements in the list must be strings.")
    return sorted(word_list)

if __name__ == '__main__':
    sample_words = ["banana", "apple", "cherry", "date", "elderberry"]
    try:
        sorted_list = sort_words(sample_words)
        print(*sorted_list)
    except ValueError as e:
        print(e)