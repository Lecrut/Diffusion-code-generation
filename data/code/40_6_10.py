import sys

def get_first_letters(input_text: str) -> list[str]:
    """Extracts the first letter of each word from the input text."""
    words = input_text.split()
    
    if not any(words):
        return []
        
    letters_list = [word[0] for word in words]
    return letters_list

if __name__ == '__main__':
    sample_input = """Hello world. 
This is a test script running locally without user input or network access.
Python scripting provides powerful ways to process text data efficiently."""

    result_letters = get_first_letters(sample_input)

    # Print each letter on a new line as per the requirement logic for readability
    print("\n".join(result_letters))