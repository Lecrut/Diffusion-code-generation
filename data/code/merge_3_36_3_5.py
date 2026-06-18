def print_reversed_sentence():
    """Prints a sentence in reverse order."""
    
if __name__ == '__main__':
    sample_sentence = "Hello, World!"
    reversed_text = ""
    # Iterate through the characters of the string backwards to build the reversed version
    for index in range(len(sample_sentence) - 1, -1, -1):
        character = sample_sentence[index]
        reversed_text += character
    
    print(reversed_text)