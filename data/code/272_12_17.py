def sort_words(words):
    if not all(isinstance(word, str) for word in words):
        raise ValueError("All elements in the list must be strings.")
    return sorted(words)

if __name__ == '__main__':
    sample_words = ["banana", "apple", "cherry"]
    print(sort_words(sample_words))