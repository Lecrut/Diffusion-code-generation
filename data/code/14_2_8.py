class VolumeComparator:
    """Encapsulates logic for comparing two volumes."""

    @staticmethod
    def compare(volume1, volume2):
        """
        Compare two volumes.

        Args:
            volume1 (float or int): The first volume value.
            volume2 (float or int): The second volume value.

        Returns:
            tuple: A tuple containing the comparison result ('less', 'equal', or 'greater')
                   and the numerical difference between volume1 and volume2.
        """
        # Ensure inputs are numeric to avoid errors during calculation
        try:
            num1 = float(volume1)
            num2 = float(volume2)
        except (TypeError, ValueError):
            raise TypeError("Both input values must be convertible to numbers.")

        difference = num1 - num2

        if num1 < num2:
            comparison_result = "less"
        elif num1 > num2:
            comparison_result = "greater"
        else:
            comparison_result = "equal"

        return (comparison_result, difference)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    vol_a = 10.5
    vol_b = 7.2
    
    result_tuple = VolumeComparator.compare(vol_a, vol_b)
    
    comparison_result, difference = result_tuple
    
    print(f"Comparing {vol_a} and {vol_b}")
    print(f"Result: {comparison_result}, Difference: {difference:.4f}")

    # Additional test cases to demonstrate functionality
    test_cases = [
        (5.0, 10.0),   # less case
        (3.0, 3.0),    # equal case
        (-2.5, -8.5)   # greater case (since -2.5 > -8.5)
    ]

    print("\nAdditional Test Cases:")
    for v1, v2 in test_cases:
        res = VolumeComparator.compare(v1, v2)[0]
        diff = abs(VolumeComparator.compare(v1, v2)[1]) if not (v1 > v2) else -VolumeComparator.compare(v1, v2)[1] 
        # Re-calculate difference correctly based on the specific call to ensure consistency in print logic above vs below
        
    for test_v1, test_v2 in [
        (5.0, 10.0),   # less case
        (3.0, 3.0),    # equal case
        (-2.5, -8.5)   # greater case (since -2.5 > -8.5)
    ]:
        r = VolumeComparator.compare(test_v1, test_v2)[0]
        d = VolumeComparator.compare(test_v1, test_v2)[1]
        print(f"{test_v1} vs {test_v2}: Result={r}, Difference={d}")