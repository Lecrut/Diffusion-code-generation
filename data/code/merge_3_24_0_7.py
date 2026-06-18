def check_number_is_negative(number: float) -> bool:
    """
    Determines if a given number is negative.

    Args:
        number (float): The numerical value to evaluate.

    Returns:
        bool: True if the number is less than zero, False otherwise.
    """
    return number < 0

def main():
    # Hard-coded sample values for testing without user input or network access.
    test_cases = [10, -5, 0.0, -3.14]

    print("Running automated tests with hard-coded numbers...")
    
    for num in test_cases:
        result = check_number_is_negative(num)
        status_str = "IS negative" if result else "is NOT negative"
        
        # Ensure no interactive prompts occur; this block is fully self-contained.
        print(f"The number {num} {status_str}.")

if __name__ == '__main__':
    main()