def process_string(s: str) -> tuple[str, str, str]:
    """
    Returns a tuple containing:
        1. The original string.
        2. The lowercase version of the string.
        3. A new string where all characters are swapped to their opposite case 
           (uppercase becomes lowercase and vice versa).
    
    Uses built-in string methods only.
    """
    lower_version = s.lower()
    # Create reversed case by converting each character: if upper, make lower; else make upper
    def swap_case_char(c):
        return c.swapcase()
    swapped_version = "".join(swap_case_char(c) for c in s)
    
    return (s, lower_version, swapped_version)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or files.
    test_input = "Hello World!"
    result = process_string(test_input)
    print(f"Original: {result[0]}")
    print(f"Lowercase: {result[1]}")
    print(f"Swapped Case: {result[2]}")