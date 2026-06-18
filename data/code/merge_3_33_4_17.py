import re

def filter_alphanumeric(text: str) -> str:
    """
    Removes all non-alphanumeric characters from the input string, including spaces.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string containing only alphanumeric characters.
    """
    return re.sub(r'[^a-zA-Z0-9]', '', text)

if __name__ == '__main__':
    # Hard-coded sample values for testing without any external input or files
    test_cases = [
        "Hello, World! 123",
        "C++ Programming: A Modern Approach!",
        "Spaces and   tabs  here  @#$%",
        ""
    ]

    results = []
    for text in test_cases:
        cleaned_text = filter_alphanumeric(text)
        results.append(f"Input: '{text}' -> Output: '{cleaned_text}'")

    # Print all results to console as part of the runnable module execution