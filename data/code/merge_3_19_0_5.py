def get_number(prompt):
    """Prompt the user (or use default) to enter a number."""
    # Since input() is forbidden in interactive mode per constraints, 
    # this function will raise an error if truly called interactively without defaults,
    # but for the sample block we pass values directly.
    try:
        return float(prompt.strip())
    except ValueError as e:
        print(f"Error converting input to number: {e}")
        raise

def is_first_greater_than_second(num1, num2):
    """Check if the first number is strictly greater than the second."""
    return num1 > num2

if __name__ == '__main__':
    # Hard-coded sample values as per requirement to avoid input() calls
    sample_num1 = 50.5
    sample_num2 = 49.8
    
    try:
        result = is_first_greater_than_second(sample_num1, sample_num2)
        
        if result:
            print(f"The first number ({sample_num1}) is strictly greater than the second number ({sample_num2}).")
        else:
            print(f"The first number ({sample_num1}) is not strictly greater than the second number ({sample_num2}).")
            
    except Exception as e:
        # Fallback error handling for unexpected issues in sample block execution
        print("An unexpected error occurred during evaluation.")