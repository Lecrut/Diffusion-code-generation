import sys

def validate_input_string(s: str) -> bool:
    """Validate that the input string is non-empty."""
    return len(s.strip()) > 0

def apply_swap_case(text: str) -> str:
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
    return "".join(result)

def process_string(input_data: str):
    """Process the input string based on a predefined rule."""
    if not validate_input_string(input_data):
        raise ValueError("Input validation failed: String must be non-empty.")

    # Apply the 'swap' case manipulation rule to the entire string
    output = apply_swap_case(input_data)
    
    return output

if __name__ == '__main__':
    try:
        # Hard-coded sample values as per requirements (no user input, args, or network access)
        sample_input_1 = "Hello World! 123"
        sample_input_2 = ""

        print("Processing Sample Input 1:")
        result_1 = process_string(sample_input_1)
        print(f"Original: {sample_input_1}")
        print(f"Result (Swap Case): {result_1}\n")

        # Test edge case with empty string to demonstrate error handling logic, 
        # though the sample block itself doesn't trigger an exception if we handle it gracefully or skip.
        # To strictly follow 'run without user input', we will process a valid hardcoded value only for output.
        
    except ValueError as e:
        print(f"Error during processing: {e}", file=sys.stderr)
        sys.exit(1)