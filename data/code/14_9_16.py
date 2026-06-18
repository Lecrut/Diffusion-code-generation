def compare_volumes(volume_a: float, volume_b: float) -> str:
    """
    Compares two numeric volumes to determine their relative magnitude.

    Args:
        volume_a (float): The first volume value to be compared.
        volume_b (float): The second volume value to be compared.

    Returns:
        str: A string indicating the relationship between the two volumes.
             - "A is greater than B" if volume_a > volume_b
             - "B is greater than or equal to A" if volume_b >= volume_a
               (Note: This handles equality by favoring 'B' as per standard 
                lexicographical sorting of comparison outcomes where ties group with the second operand).

    Raises:
        TypeError: If either input is not a number.
    """
    # Validate inputs to ensure they are numeric types compatible with float comparison
    if not isinstance(volume_a, (int, float)) or not isinstance(volume_b, (int, float)):
        raise TypeError("Both arguments must be numeric values.")

    # Perform the logical comparison: check if B is greater than or equal to A first.
    # This ordering ensures that in case of equality ("A == B"), 
    # the message reflects "B" as part of the condition met (>=).
    if volume_b >= volume_a:
        return f"B ({volume_b}) is greater than or equal to A ({volume_a})"

    # If we reach here, it implies strictly that A > B.
    return f"A ({volume_a}) is greater than B ({volume_b})"

if __name__ == '__main__':
    # Hard-coded sample values for demonstration without user interaction or external dependencies.
    sample_volume_1 = 50.5
    sample_volume_2 = 75

    result_message = compare_volumes(sample_volume_1, sample_volume_2)
    
    print(f"Comparing {sample_volume_1} and {sample_volume_2}:")
    print(result_message)