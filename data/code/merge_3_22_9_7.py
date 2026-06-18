def is_odd_bitwise(n: int) -> bool:
    """
    Determine if an integer is odd using bitwise operations instead of modulo.
    
    An integer n is odd if its least significant bit (LSB) is 1.
    The expression (n & 1) returns the LSB as either 0 or 1.
    Therefore, checking if (n & 1) equals 1 determines oddness.

    Args:
        n: Integer to check.

    Returns:
        True if n is odd, False otherwise.
    """
    return bool(n & 1)

if __name__ == '__main__':
    # Hard-coded sample values for testing without any user input or external dependencies
    test_values = [-5, -4, 0, 1, 2, 3, 7]

    print("Testing oddness using bitwise AND operation:")
    for val in test_values:
        result = is_odd_bitwise(val)
        status = "Odd" if result else "Even"
        # Verify correctness against known math behavior (n % 2 != 0 for negative numbers too)
        expected_math = val % 2 != 0
        assert result == expected_math, f"Mismatch for {val}"
        print(f"{val:4d} -> Bitwise Odd Check ({status})")

    # Demonstrate the operation explicitly with a few examples
    sample_numbers = [15, 8]
    print("\nExplicit bitwise check:")
    for num in sample_numbers:
        bit_result = num & 1
        is_odd_check = bool(bit_result)
        print(f"{num} binary ends with {bin(num)[-2:]}. LSB value: {bit_result}. Is Odd? {is_odd_check}")