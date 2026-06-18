import sys

def reverse_string(text: str) -> str:
    """
    Reverses the order of characters in the input string.
    
    Args:
        text (str): The input string to be reversed.
        
    Returns:
        str: The reversed string.
    """
    return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user interaction or inputs
    sample_inputs = [
        "Hello, World!",
        "Python",
        "",
        "12345"
    ]
    
    for input_str in sample_inputs:
        reversed_result = reverse_string(input_str)
        print(f'Input:  "{input_str}"')
        print(f'Output: "{reversed_result}"\n')