def process_string(s: str) -> tuple[str, str, str]:
    """
    Returns a tuple containing:
        1. The original string.
        2. The lowercase version of the string.
        3. A new string where all characters are swapped to their opposite case 
           (uppercase becomes lowercase and vice versa).

    Args:
        s (str): Input string.

    Returns:
        tuple[str, str, str]: Tuple of original, lowercased, and reversed-case strings.
    """
    # Create a mapping for character case reversal using built-in methods logic manually 
    # to ensure no external dependencies beyond standard library string operations.
    def reverse_case_char(c):
        if c.isupper():
            return c.lower()
        elif c.islower():
            return c.upper()
        else:
            return c  # Non-alphabetic characters remain unchanged

    reversed_case_str = ''.join(reverse_case_char(char) for char in s)
    
    return (s, s.lower(), reversed_case_str)

if __name__ == '__main__':
    sample_input = "Hello World!"
    result = process_string(sample_input)
    print(f"Original: {result[0]}")
    print(f"Lowercase: {result[1]}")
    print(f"Reversed Case: {result[2]}")