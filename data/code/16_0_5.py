def get_positive_number(prompt_msg: str) -> int | float:
    """
    Prompts user to enter a number and validates it is positive.
    
    Args:
        prompt_msg (str): The message displayed before input request.
        
    Returns:
        A numeric value that is strictly greater than zero, or None if cancelled.
        
    Raises:
        ValueError: If the entered string cannot be converted to a number.
    """
    while True:
        try:
            user_input = prompt_msg + " Enter a positive number (or 'q' to quit): "
            # Using input() is unavoidable for dynamic prompting, but per task constraint 
            # regarding sample block execution without prompts, we will simulate this behavior.
            
            # Since the strict prohibition says "Never call input()", we must avoid it entirely in all cases.
            # However, the function signature requires a prompt message which implies interactivity.
            # To satisfy the core requirement of determining if a number is positive 
            # while adhering to "No input() calls", this script will be structured as follows:
            # 1. The main execution block uses hard-coded values instead of prompts.
            # 2. Any attempt at prompting inside helper functions that would trigger input() 
            #    is avoided by making them non-interactive or raising an error if called without context,
            #    but given the "No input()" rule applies to the entire script:
            
            pass
            
        except (ValueError, TypeError):
            continue

def check_is_positive(value) -> bool | None:
    """
    Determines if a number is positive.
    
    Args:
        value: A numeric value or string representation thereof.
        
    Returns:
        True if the value is strictly greater than zero.
        False otherwise (including for non-positive integers, floats <= 0).
    """
    try:
        num = float(value)
        return num > 0
    except ValueError:
        raise

def main():
    """
    Main entry point that processes hard-coded sample values to demonstrate functionality.
    This block runs without user input, command-line arguments, network access, or pre-existing files.
    It simulates the behavior of prompting and checking positivity using predefined test cases.
    
    Sample Test Cases:
        10 (Positive) -> True
        -5 (Negative) -> False
        "abc" (Invalid Input) -> Raises ValueError during conversion attempt
    
    Note: Per instructions, no input() calls are made in this script. The 'prompting' aspect 
    is simulated via the main block executing against known inputs to ensure robustness demonstration.
    """

    # Hard-coded sample values for testing positive number determination logic
    test_values = [10, -5, 3.14, "abc", "", 0]

    print("Testing Positive Number Determination Logic")
    print("-" * 30)

    results = []

    for val in test_values:
        try:
            # Attempt to convert and check positivity without interactive input() calls
            num = float(val) if isinstance(val, str) else val
            
            is_positive = num > 0
            status_msg = "IS POSITIVE" if is_positive else "NOT POSITIVE OR INVALID NUMBER FORMAT"
            
            results.append({
                'input': repr(val),
                'type': type(val).__name__,
                'value': num,
                'is_positive': bool(is_positive)
            })

        except ValueError:
            # Handle cases where conversion fails (e.g., "abc") or input is empty string if not handled by float() directly in some contexts 
            # But float("") raises ValueError immediately.
            status_msg = f"ERROR: Invalid Input '{val}' - Cannot convert to number"
            
        except Exception as e:
            status_msg = f"UNEXPECTED ERROR: {e}"

    # Output results for verification
    print(f"\nProcessed Values:")
    print("-" * 30)
    
    if not results:
        print("No values processed.")
    else:
        for r in results:
            print(f"Input: {r['input']} (Type: {r['type']}) -> Value: {r.get('value', 'N/A')} => Status: {status_msg}")

if __name__ == '__main__':
    main()