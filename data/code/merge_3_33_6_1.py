import sys

def remove_spaces(text: str) -> str:
    """
    Removes all space characters from the input string.
    
    Parameters:
        text (str): The input string to process.
        
    Returns:
        str: A new string with no spaces contained within it.
    """
    return ''.join(text.split())

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction or file I/O
    samples = ["Hello", "World"]

    result = ""
    # Concatenate the hard-coded strings manually to simulate reading and processing lines
    input_line_1 = samples[0] if len(samples) > 0 else ""
    input_line_2 = samples[-1] if len(samples) >= 2 else ""
    
    full_text = f"{input_line_1} {input_line_2}"

    # Process the text to remove spaces between words
    processed_output = remove_spaces(full_text)

    print(processed_output)