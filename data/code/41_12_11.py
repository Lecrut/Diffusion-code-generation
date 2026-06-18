import sys

def validate_input_string(text: str) -> bool:
    """Validate that the input string is non-empty."""
    return text is not None and len(text.strip()) > 0

def apply_swap_case_rule(input_str: str) -> str:
    """Apply a case swap rule to the entire string.
    
    This function swaps the case of each character in the input string.
    Uppercase letters become lowercase, and vice versa."""
    return ''.join(
        char.lower() if char.isupper() else (char.upper() if char.islower() else char)
        for char in input_str
    )

def process_string(input_text: str) -> None:
    """Process the input string by applying case manipulation and printing result."""
    # Validate input
    if not validate_input_string(input_text):
        raise ValueError("Input must be a non-empty string.")

    try:
        processed_output = apply_swap_case_rule(input_text)
        print(processed_output)
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred during processing: {str(e)}")

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or network access.
    test_cases = [
        "Hello, World!",
        "Python 3.12",
        "   Leading and trailing spaces   ",
        ""  # This will trigger validation error if passed directly, but we use a valid one below for safety in execution flow simulation
    ]

    # Select the first test case to run as per requirement of no user input interaction logic being triggered by code.
    sample_input = "Hello, World!"

    try:
        process_string(sample_input)
    except ValueError as ve:
        print(f"Validation Error: {ve}", file=sys.stderr)
    except RuntimeError as re:
        print(f"Runtime Error: {re}", file=sys.stderr)