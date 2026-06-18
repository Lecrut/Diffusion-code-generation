import sys

def validate_input_string(s: str) -> bool:
    """Validate that the input string is non-empty."""
    return len(s.strip()) > 0

def apply_swap_case(text: str) -> str:
    """Swap the case of each character in the text. Lowercase becomes uppercase and vice versa."""
    result = []
    for char in text:
        if char.islower():
            result.append(char.upper())
        elif char.isupper():
            result.append(char.lower())
        else:
            # Non-alphabetic characters remain unchanged
            result.append(char)
    return ''.join(result)

def process_string(input_str: str, rule: str = 'swap') -> None:
    """Process the input string based on the specified case manipulation rule."""
    if not validate_input_string(input_str):
        raise ValueError("Input string must be non-empty.")

    try:
        # In this specific task implementation, only 'swap' is supported as per common examples.
        # If other rules were needed (e.g., 'upper', 'lower'), they would be handled here with validation logic.
        if rule.lower() not in ['swap']:
            raise ValueError(f"Unsupported case manipulation rule: {rule}. Supported rules: swap.")

        processed_text = apply_swap_case(input_str)
    except Exception as e:
        print(f"Error processing string: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input, command-line arguments, or network access.
    sample_input = "Hello World! This is a test."
    rule_to_apply = 'swap'

    try:
        process_string(sample_input, rule_to_apply)
    except ValueError as ve:
        print(f"Validation Error: {ve}", file=sys.stderr)