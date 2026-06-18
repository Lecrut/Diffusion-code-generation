def is_even(n):
    """
    Check if a given integer n is even using bitwise operations.
    
    This method leverages the fact that an integer's least significant bit (LSB) 
    is 1 for odd numbers and 0 for even numbers in binary representation.
    Performing a bitwise AND with 1 isolates this LSB.

    Args:
        n (int): The integer to check.

    Returns:
        bool: True if n is even, False otherwise.
    
    Performance Note: 
        Bitwise operations are generally faster than modulo arithmetic in tight loops,
        though the difference is negligible for most general use cases. This approach
        also avoids any potential issues with overflow or zero handling inherent to division logic.

    Readability Note:
        The `n & 1 == 0` construct (or its negation) reads naturally as a mathematical condition 
        and remains idiomatic in Python compared to alternative bit manipulation tricks that obscure intent,
        such as converting n to binary or using complex boolean algebra with the result.

    :param int n: The input integer.
    :return bool: True if even, False otherwise.
    """
    return (n & 1) == 0

if __name__ == '__main__':
    # Sample values for testing without user interaction or external dependencies.
    
    test_cases = [2, -4, 0, 3, 57]

    print("Testing even number check function:")
    for value in test_cases:
        result = is_even(value)
        status = "Even" if result else "Odd"
        print(f"{value} -> {status}")