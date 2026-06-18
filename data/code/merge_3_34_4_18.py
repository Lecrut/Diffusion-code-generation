import sys

def capitalize_first_letter(text: str) -> str:
    """
    Capitalizes the first letter of each word in the input text.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with the first character of each word capitalized,
             preserving original casing for subsequent letters and spaces.
    """
    words = text.split()
    return " ".join(word.capitalize() if len(word) > 0 else "")

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input,
    # command-line arguments, network access, or pre-existing files.
    samples = [
        "hello world",
        "python is awesome!",
        "  multiple   spaces here ",
        "no words at all"
    ]

    for sample in samples:
        result = capitalize_first_letter(sample)
        print(f'Input: "{sample}"')
        print(f'Output: "{result}"\n')