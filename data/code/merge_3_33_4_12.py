import re

def filter_alphanumeric(text: str) -> str:
    """
    Removes all non-alphanumeric characters from the input string, including spaces.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string containing only alphanumeric characters in their original order.
    """
    # Regular expression matches any character that is a letter or a digit
    return re.sub(r'[^a-zA-Z0-9]', '', text)

if __name__ == '__main__':
    sample_string = "Hello, World! This is a test... 123"
    result = filter_alphanumeric(sample_string)
    print(result)