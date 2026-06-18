def parse_integer(value: str) -> int | None:
    """Attempts to convert a string representation of an integer into an integer."""
    try:
        # Check if it's already a valid integer format or contains whitespace around digits
        stripped = value.strip()
        result = int(stripped)
        return result
    except ValueError:
        return None

def are_numbers_equal(str_num1: str, str_num2: str) -> bool:
    """Checks if two string inputs represent equal numerical values."""
    num1 = parse_integer(str_num1)
    num2 = parse_integer(str_num2)
    
    # If either input is not a valid integer representation, they are considered unequal.
    return num1 == num2

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction
    test_value_1 = "42"
    test_value_2 = "-789"
    
    result = are_numbers_equal(test_value_1, test_value_2)
    
    print(f"{test_value_1} and {test_value_2}: {'Equal' if result else 'Not Equal'}")

# Additional robustness check for edge cases like " 42 " or leading zeros