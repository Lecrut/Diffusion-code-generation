def sort_words(words):
    if not all(isinstance(word, str) for word in words):
        raise ValueError("All elements in the list must be strings.")
    return sorted(words)

if __name__ == '__main__':
    sample_list = ["banana", "apple", "cherry", "date", "elderberry"]
    try:
        sorted_list = sort_words(sample_list)
        print(sorted_list)
    except ValueError as e:
        print(e)