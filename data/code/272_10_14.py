def sort_words(words):
    if not isinstance(words, list) or not all(isinstance(word, str) for word in words):
        raise ValueError("Input must be a list of strings")
    
    return sorted(words)

if __name__ == '__main__':
    sample_words = ["banana", "apple", "cherry"]
    try:
        sorted_words = sort_words(sample_words)
        print(sorted_words)
    except ValueError as e:
        print(e)