def reverse_word(word: str) -> str:
    """Reverse a given word."""
    return ''.join(reversed(list(word)))

if __name__ == '__main__':
    sample_word = "Python"  # Hard-coded sample value for testing without user input
    
    if not isinstance(sample_word, (str)) or len(sample_word) == 0:
        print("Error: The sample word must be a non-empty string.")
    else:
        reversed_word = reverse_word(sample_word)
        result = f"Original Word: {sample_word}\nReversed Word: {reversed_word}"
        print(result)