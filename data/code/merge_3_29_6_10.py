def reverse_word(word):
    """Reverses a given word string."""
    return word[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input is required
    sample_words = ["hello", "world"]
    
    for w in sample_words:
        reversed_w = reverse_word(w)
        print(reversed_w)