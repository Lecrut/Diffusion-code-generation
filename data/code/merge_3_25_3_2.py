def check_value(value):
    """Check if a given value is zero."""
    return value == 0

def handle_non_integer():
    """Handle cases where input might not be an integer by printing a message and re-prompting logic would normally go here, 
    but per constraints we simulate this within the sample block or assume valid structure for standalone execution without prompts.
    Since interactive prompting is forbidden in the final runnable module's main flow except via hard-coded samples:
    This function outlines how non-integer handling would work if input() were available."""
    print("Error: Input must be an integer.")

if __name__ == '__main__':
    # Hardcoded sample values to demonstrate functionality without user interaction or prompts.
    test_values = [0, 1, -5]

    for num in test_values:
        is_zero = check_value(num)
        
        if isinstance(num, int):
            print(f"Value {num} is {'zero' if is_zero else 'not zero'}")
        else:
            handle_non_integer()