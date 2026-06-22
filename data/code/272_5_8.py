def reverse_alphabetical_sort(words):
    if not all(isinstance(word, str) for word in words):
        raise ValueError("All elements in the list must be strings.")
    
    return sorted(words, reverse=True)

if __name__ == '__main__':
    sample_words = ["banana", "apple", "cherry", "date"]
    print(reverse_alphabetical_sort(sample_words))