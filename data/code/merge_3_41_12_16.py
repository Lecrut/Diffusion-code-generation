import sys

def validate_input_string(s):
    """Validates that the input string is a non-empty sequence of characters."""
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")
    if len(s) == 0:
        raise ValueError("Input string cannot be empty.")

def apply_swap_case_rule(text):
    """Swaps the case of each character in the input string."""
    return text.swapcase()

def main():
    # Hard-coded sample values to ensure no user interaction or files are accessed.
    test_cases = [
        "Hello, World!",
        "",  # Edge case: empty string (should raise ValueError)
        "123 !@#",  # Contains non-alphabetic characters
    ]

    for index, input_string in enumerate(test_cases):
        try:
            validate_input_string(input_string)
            
            if not isinstance(input_string, str) or len(input_string) == 0:
                raise ValueError("Invalid string format.")
                
            result = apply_swap_case_rule(input_string)
            print(f"Input {index}: '{input_string}' -> Output: '{result}'")
        except (ValueError, TypeError) as e:
            # Comprehensive error handling for validation failures.
            if index == 1 and len(input_string) == 0:
                print(f"Error at step {index} ({type(e).__name__}): Input string cannot be empty.")
            else:
                print(f"Error processing input {index}: {e}")

if __name__ == '__main__':
    main()