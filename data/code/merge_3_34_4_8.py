import sys

def capitalize_first_letter(text: str) -> str:
    """
    Capitalizes only the first letter of each word in the input text.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with the first letter of each word capitalized,
             while preserving the original casing for all other letters.
    """
    words = text.split()
    return ' '.join(word.capitalize() if len(word) > 0 else '')

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input,
    # command-line arguments, network access, or pre-existing files.
    sample_texts = [
        "hello world this is a test",
        "python programming language fun",
        "   leading spaces and trailing ones  ",
    ]

    for text in sample_texts:
        print(f"Input: '{text}'")
        result = capitalize_first_letter(text)
        print(f"Output: '{result}'")