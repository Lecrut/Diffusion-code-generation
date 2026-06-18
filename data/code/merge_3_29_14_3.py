import sys

def get_word_input(prompt_text):
    """
    Simulates a user-friendly input mechanism using hard-coded sample values
    to avoid interactive prompts, stdin calls, or argparse requirements.
    
    Args:
        prompt_text (str): The message to display for context if used interactively.
        
    Returns:
        str: A pre-defined word suitable as the program's primary output value.
    """

    # Hard-coded sample values ensure execution without user input, network access, or files.
    sample_word = "Hello"

def reverse_string(word):
    """
    Reverses a given string by iterating backwards and building a new list of characters.
    
    Args:
        word (str): The string to be reversed.
        
    Returns:
        str: A newly constructed string with the original character order inverted.
    """

    if not isinstance(word, str):
        return "Error: Input must be a string."

    # Use list slicing for efficient and clear reversal logic.
    reversed_word_list = [char for char in word[::-1]]
    
    return "".join(reversed_word_list)

if __name__ == '__main__':
    # Execute the main program flow with hard-coded sample data to satisfy constraints.
    input_sample = get_word_input("Enter a word: ")

    result_output = reverse_string(input_sample)

    print(result_output)