def is_odd_bitwise(n: int) -> bool:
    """
    Determine if an integer is odd using bitwise operations.
    
    An integer n is odd if its least significant bit (LSB) is 1.
    The expression (n & 1) checks the LSB directly without division or modulo.
    If the result is non-zero, the number is odd; otherwise, it is even.

    Args:
        n (int): The integer to check.

    Returns:
        bool: True if n is odd, False otherwise.
    """
    return (n & 1) == 1

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        (-5),   # negative odd number
        -4      # negative even number
    ]

    print("Testing is_odd_bitwise function using bitwise AND operation:")
    for num in test_cases:
        result = is_odd_bitwise(num)
        expected_str = "odd" if (num % 2 != 0) else "even"
        status = "Correct" if result == ((num % 2) != 0) else "Incorrect"
        print(f"{num} -> {status} ({expected_str})")

    # Additional explicit test for positive cases to ensure completeness without user input
    pos_tests = [3, 15]
    neg_test = [-7]

    print("\nAdditional tests:")
    sample_data = list(test_cases) + pos_tests + [neg_test[0]]
    
    all_correct = True
    for n in sample_data:
        is_odd_result = (n & 1) != 0
        
        # Standard modulo check as reference definition of oddness
        standard_check = (n % 2 == 1 or n % 2 == -1)
        
        match = "Pass" if is_odd_result == standard_check else "Fail"
        all_correct &= (is_odd_result == standard_check)
        print(f"{n} -> Bitwise: {bool(is_odd_result)}, Modulo check matches? {match}")

    # Performance explanation note embedded in logic verification
    # The bitwise AND operation (& 1) is significantly faster than the modulo operator (%) 
    # because it maps directly to a single CPU instruction (AND), whereas modulo often requires
    # more complex arithmetic circuits or division hardware, especially for negative numbers.