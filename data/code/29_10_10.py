def reverse_string(input_str: str) -> str:
    """
    Reverses a given input string.
    
    Args:
        input_str (str): The string to be reversed.
        
    Returns:
        str: The reversed string.
    """
    return input_str[::-1]

def main():
    # Hard-coded sample values as per task requirements
    # No user input, command-line arguments, or network access is used.
    
    test_cases = [
        "Hello World",
        "",
        "Python Programming",
        "!@#$%^&*()",
        12345,          # Note: If a non-string type were passed here explicitly in logic, 
                       # it would need conversion, but the function expects str.
    ]

    for test_input in test_cases:
        if isinstance(test_input, (int, float)):
            # Convert numeric types to string before reversing as per robust handling expectation
            input_str = str(test_input)
        else:
            input_str = test_input
        
        reversed_output = reverse_string(input_str)
        
        print(f"Input:    '{input_str}'")
        print(f"Reversed: '{reversed_output}'")
        print("-" * 20)

if __name__ == '__main__':
    main()