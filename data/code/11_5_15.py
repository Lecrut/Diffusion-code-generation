def find_ratio_of_lengths(l1: int, l2: int) -> tuple[int, int]:
    """
    Calculates the simplified ratio of two integer lengths using the Euclidean algorithm.
    
    Args:
        l1 (int): First length value.
        l2 (int): Second length value.
        
    Returns:
        tuple[int, int]: A tuple containing the numerator and denominator of the 
                         simplified fraction representing the ratio.
                         
    Raises:
        ValueError: If either input is non-positive or if inputs are not integers.
    """
    # Validate inputs to ensure they are positive integers for a valid geometric ratio
    if l1 <= 0 or l2 <= 0:
        raise ValueError("Lengths must be positive integers.")
    
    def euclidean_algorithm(a: int, b: int) -> int:
        """Helper function to calculate the Greatest Common Divisor (GCD)."""
        while b != 0:
            a, b = b, a % b
        return abs(a)

    # Calculate GCD of l1 and l2
    gcd_value = euclidean_algorithm(l1, l2)

    # Simplify the ratio by dividing both lengths by their GCD
    simplified_l1 = l1 // gcd_value
    simplified_l2 = l2 // gcd_value

    return (simplified_l1, simplified_l2)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or files.
    
    # Test Case 1: Standard integers with a common factor greater than 1
    result_1 = find_ratio_of_lengths(8, 4)
    print(f"Ratio of 8 and 4 is {result_1}")

    # Test Case 2: Co-prime numbers (GCD should be 1)
    result_2 = find_ratio_of_lengths(5, 7)
    print(f"Ratio of 5 and 7 is {result_2}")

    # Test Case 3: Large integers with a common factor
    result_3 = find_ratio_of_lengths(90, 18)
    print(f"Ratio of 90 and 18 is {result_3}")