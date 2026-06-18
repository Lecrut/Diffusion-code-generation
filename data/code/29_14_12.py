def reverse_word(word):
    """Reverses a given word string."""
    return word[::-1]

if __name__ == '__main__':
    # Sample input to ensure the program runs without user interaction or arguments
    sample_values = ["Hello", "Python"]
    
    for val in sample_values:
        reversed_word = reverse_word(val)
        print(f"Original: {val}")
        print("Reversed:", reversed_word)