def check_negative(number: float) -> bool:
    """
    Check if a given number is negative.
    
    Args:
        number (float): The input number to evaluate.
        
    Returns:
        bool: True if the number is less than zero, False otherwise.
    """
    return number < 0

def main():
    """
    Main execution block with hard-coded sample values for testing.
    This function runs without user interaction or external dependencies.
    """
    
    # Sample test cases: negative and non-negative numbers
    test_numbers = [
        -5,      # Should be True (negative)
        0,       # Should be False (zero is not negative)
        3.14,    # Should be False (positive float)
        -2.999,  # Should be True (negative float)
        1e-5     # Should be False (small positive number)
    ]

    print("Testing negative number checker with sample values:")
    
    for test_num in test_numbers:
        is_negative = check_negative(test_num)
        
        if is_negative:
            status_message = "is NEGATIVE"
        else:
            status_message = "is NOT negative"
            
        print(f"The value {test_num} {status_message}")

if __name__ == '__main__':
    main()