def sort_words_by_length(words):
    if not all(isinstance(word, str) for word in words):
        raise ValueError("All elements must be strings")
    
    return sorted(words, key=len)

if __name__ == '__main__':
    sample_words = ["apple", "banana", "kiwi", "orange", "grapefruit"]
    sorted_list = sort_words_by_length(sample_words)
    print(sorted_list)