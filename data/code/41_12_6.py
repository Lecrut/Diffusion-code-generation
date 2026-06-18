import sys

def validate_input_string(s: str) -> bool:
    """Validate that the input string is non-empty."""
    return len(s.strip()) > 0

def swap_case(text: str) -> str:
    """Swap the case of each character in the text. Uppercase becomes lowercase and vice versa."""
    result = []
    for char in text:
        if char.isupper():
            result.append(char.lower())
        elif char.islower():
            result.append(char.upper())
        else:
            # Preserve non-alphabetic characters (digits, symbols, spaces) as is
            result.append(char)
    return ''.join(result)

def process_string(input_str: str, rule: str = 'swap') -> None:
    """Process the input string based on the specified rule and print the result."""
    if not validate_input_string(input_str):
        raise ValueError("Input string must be non-empty.")

    try:
        # Implementing only the 'swap' case manipulation as per common examples.
        # Other rules like 'upper', 'lower', or 'capitalize' could be added here in a production scenario.
        if rule.lower() == 'swap':
            processed_text = swap_case(input_str)
        else:
            raise ValueError(f"Unsupported transformation rule '{rule}'. Supported: 'swap'.")

        print(processed_text)

    except Exception as e:
        # Comprehensive error handling for unexpected issues during processing
        if isinstance(e, (ValueError, TypeError)):
            sys.stderr.write(f"Input Error: {str(e)}\n")
        else:
            sys.stderr.write(f"Unexpected Error: {type(e).__name__}: {str(e)}\n")

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input, 
    # command-line arguments, network access, or pre-existing files.
    
    # Sample inputs for testing different scenarios including edge cases
    
    test_cases = [
        "Hello World!",           # Standard mixed case with punctuation and space
        "",                       # Empty string (should trigger validation error)
        "PYTHON IS COOL",         # All uppercase
        "python is cool",         # All lowercase
        "12345 !@#",              # Non-alphabetic characters only
    ]

    for test_input in test_cases:
        try:
            process_string(test_input, rule='swap')
        except ValueError as ve:
            print(f"Validation Failed for input '{test_input}': {ve}", file=sys.stderr)