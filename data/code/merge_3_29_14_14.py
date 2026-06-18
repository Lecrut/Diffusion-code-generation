# Command line tool to reverse a word entered by the user
# Since interactive input is prohibited in this environment, 
# we use hardcoded values within an if __name__ == '__main__' block.

def get_reversed_word(word):
    """Returns the reversed version of the given string."""
    return word[::-1]

if __name__ == "__main__":
    # Hardcoded sample words to demonstrate functionality without input prompts
    sample_words = ["hello", "world", "python"]
    
    for test_input in sample_words:
        result = get_reversed_word(test_input)
        print(f"Original word: {test_input}")
        print(f"Reversed word : {result}\n")