import re

def filter_alphanumeric(text: str) -> str:
    """
    Returns a new string containing only alphanumeric characters from the input.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A string with all non-alphanumeric and whitespace characters removed.
    """
    return re.sub(r'[^a-zA-Z0-9]', '', text)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    test_cases = [
        "Hello, World! 123",
        "Python@Code#2024 & More!!!",
        "   Leading spaces and tabs\tto remove   ",
        ""
    ]

    for test_input in test_cases:
        result = filter_alphanumeric(test_input)
        print(f"Input: {repr(test_input)}")
        print(f"Output: {result}")
        print("-" * 20)