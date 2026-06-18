import re

def reverse_string(input_str: str) -> str:
    """
    Reverses a given input string using slicing, which is efficient 
    in Python compared to manual character manipulation loops.
    
    Args:
        input_str (str): The string to be reversed.
        
    Returns:
        str: A new string that is the reverse of the input.
    """
    return input_str[::-1]

def main():
    # Hard-coded sample values as per requirements; no user interaction or external inputs allowed.
    test_cases = [
        "Hello, World!",
        "",
        "Python 3.9",
        "!olleH ,dlroW",
        "   Leading spaces ",
        "1234567890"
    ]

    print("String Reversal Script")
    print("=" * 40)

    for test_input in test_cases:
        reversed_result = reverse_string(test_input)
        
        # Output formatting to ensure clarity and robustness across different input types (e.g., spaces, numbers)
        output_line = f"Input : '{test_input}'\nOutput: '{reversed_result}'"
        print(output_line)

if __name__ == '__main__':
    main()