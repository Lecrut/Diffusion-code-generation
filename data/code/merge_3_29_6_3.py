import sys

def reverse_word(word):
    """Reverses a given string."""
    return word[::-1]

if __name__ == '__main__':
    # Sample input and output as per constraints (no user interaction)
    sample_words = ["hello", "world"]
    
    for test_input in sample_words:
        reversed_word = reverse_word(test_input)
        print(f"Original: {test_input}")
        print("Reversed:", reversed_word)