import sys

def capitalize_first_letter(text: str) -> str:
    """
    Capitalizes the first letter of each word in the input text.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with the first character of each word capitalized,
             and all other characters lowercased within that word.
    """
    if not isinstance(text, str):
        return ""

    words = text.split()
    
    # Capitalize the first letter and lowercase the rest for each word
    processed_words = [word.capitalize() for word in words]
    
    return " ".join(processed_words)

if __name__ == '__main__':
    # Hard-coded sample values to ensure execution without user input or arguments.
    samples = ["hello world", "PYTHON IS FUN", "  multiple   spaces here ", "single"]

    for sample in samples:
        result = capitalize_first_letter(sample)
        print(f"Input: '{sample}'")
        print(f"Output: '{result}'\n")