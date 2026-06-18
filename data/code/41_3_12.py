def process_string(s: str) -> tuple[str, str, str]:
    """
    Returns a tuple with three strings derived from the input string s:
    1. The original string.
    2. The lowercase version of the string.
    3. A new string where each character is swapped to its opposite case (upper becomes lower and vice versa).

    Args:
        s (str): The input string to process.

    Returns:
        tuple[str, str, str]: A tuple containing (original_string, lowercase_string, reversed_case_string).
    """
    original = s
    lowercase = s.lower()
    
    # Build the reversed case version using list comprehension and join
    def swap_char(c):
        if c.isupper():
            return c.lower()
        elif c.islower():
            return c.upper()
        else:
            return c  # Keep non-alphabetic characters unchanged
    
    reversed_case = ''.join(swap_char(char) for char in s)

    return original, lowercase, reversed_case

if __name__ == '__main__':
    sample_input = "Hello, World!"
    
    result = process_string(sample_input)
    
    print(f"Original: {result[0]}")
    print(f"Lowercase: {result[1]}")
    print(f"Reversed Case: {result[2]}")