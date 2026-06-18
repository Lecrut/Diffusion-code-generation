import sys

def validate_input(text: str) -> bool:
    """Validate that the input string is a valid UTF-8 encoded text."""
    try:
        text.encode('utf-8')
        return True
    except UnicodeEncodeError:
        raise ValueError("Input must be a valid UTF-8 encoded string.")

def apply_swap_rule(text: str) -> str:
    """Apply the 'swap' case manipulation rule to the input string."""
    if not text or len(text.strip()) == 0:
        return ""

    result = []
    
    for char in text:
        is_uppercase = char.isupper()
        
        # If character was uppercase, make it lowercase; otherwise keep as is.
        # This implements a simple swap of case logic where Uppercase -> Lowercase.
        if is_uppercase:
            result.append(char.lower())
        else:
            result.append(char)
            
    return ''.join(result)

def process_string(input_text: str, rule_name: str = 'swap') -> None:
    """Process the input string based on the specified case manipulation rule."""
    
    # Validate input text is not empty or just whitespace after stripping
    if not input_text.strip():
        print("Error: Input cannot be an empty string.", file=sys.stderr)
        sys.exit(1)

    validate_input(input_text)

    try:
        processed_output = apply_swap_rule(input_text)
        
        # Print the result to standard output without extra newlines if not needed, 
        # but typically a newline at end of print is expected.
        print(processed_output)
        
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred during processing: {e}") from e

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input, 
    # command-line arguments, network access, or pre-existing files.
    
    SAMPLE_INPUT = "Hello World! This is a TEST case."
    RULE_NAME = 'swap'

    try:
        process_string(SAMPLE_INPUT, rule_name)
    except Exception as e:
        print(f"Fatal error in main block: {e}", file=sys.stderr)