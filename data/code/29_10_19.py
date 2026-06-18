import sys

def reverse_string(input_str):
    """
    Reverses a given input string.
    
    Args:
        input_str (str): The string to be reversed. If not a string, 
                         it attempts conversion or returns an error message.
        
    Returns:
        str: The reversed string.
    """
    if isinstance(input_str, str):
        return input_str[::-1]
    else:
        # Handle non-string inputs by attempting to convert them first for robustness
        try:
            converted = str(input_str)
            return converted[::-1]
        except Exception as e:
            return f"Error processing input type {type(input_str).__name__}: {str(e)}"

def main():
    """
    Main function containing the execution block.
    Runs with hard-coded sample values without user interaction,
    command-line arguments, or external dependencies.
    """
    
    # Sample inputs covering different data handling scenarios
    samples = [
        "Hello World!",
        1234567890,       # Integer input to test conversion logic inside helper
        True,              # Boolean input to test type handling
        "!olleH",          # Already reversed string (idempotent check)
        "",                # Empty string edge case
    ]
    
    output_lines = []
    
    for item in samples:
        result = reverse_string(item)
        description = f"Input Type: {type(item).__name__} | Value: {item!r}"

if __name__ == '__main__':
    pass
