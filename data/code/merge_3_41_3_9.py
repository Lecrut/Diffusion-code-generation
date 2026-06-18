def process_string(text):
    """
    Returns a tuple with:
        1. The original string.
        2. The lowercase version of the string.
        3. The reversed case version (uppercase if lower, vice versa).
    
    Args:
        text (str): Input string to process.
    
    Returns:
        tuple[str, str, str]: Original, Lowercase, Reversed Case.
    """
    original = text
    lowercase = text.lower()
    reversed_case = ''.join(char.upper() if char.islower() else char.lower() for char in text[::-1])
    return (original, lowercase, reversed_case)

if __name__ == '__main__':
    sample_input = "Hello World!"
    result = process_string(sample_input)
    print(f"Original: {result[0]}")
    print(f"Lowercase: {result[1]}")
    print(f"Reversed Case: {result[2]}")