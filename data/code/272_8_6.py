def optimized_sort(words):
    if not all(isinstance(word, str) for word in words):
        raise ValueError("All elements in the list must be strings")
    
    return sorted(words)

if __name__ == '__main__':
    sample_words = ["banana", "apple", "cherry", "date", "elderberry"]
    print("Original sequence:", sample_words)
    sorted_words = optimized_sort(sample_words)
    print("Sorted list of words:")
    for word in sorted_words:
        print(word)