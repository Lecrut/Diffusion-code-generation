def sort_words(words):
    return sorted(words)

if __name__ == '__main__':
    sample_words = ["banana", "apple", "cherry"]
    if all(isinstance(word, str) for word in sample_words):
        print(sort_words(sample_words))
    else:
        print("Error: All items in the list must be strings.")