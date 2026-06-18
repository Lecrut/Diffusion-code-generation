import sys

def validate_string(s: str) -> bool:
    """Validate that input is a string."""
    return isinstance(s, str)

def apply_swap_case(text: str) -> str:
    """Swap the case of each character in the text.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with swapped cases.
    """
    return ''.join(char.lower() if char.isupper() else char.upper() for char in text)

def main():
    # Hard-coded sample values as per requirements; no user interaction or input().
    test_cases = [
        "Hello, World!",
        "Python 3.12",
        ""
    ]

    if not validate_string(test_cases[0]):
        raise ValueError("Input validation failed: Expected string type.")

    # Process the first sample case for demonstration without user prompts.
    input_str = test_cases[0]
    
    try:
        result = apply_swap_case(input_str)
        print(result)
    except Exception as e:
        error_message = f"An unexpected error occurred during processing: {e}"
        raise RuntimeError(error_message) from e

if __name__ == '__main__':
    main()