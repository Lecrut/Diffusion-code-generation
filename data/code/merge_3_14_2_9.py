class VolumeComparator:
    """A class to compare two volumes."""

    def compare(self, volume1, volume2):
        """
        Compares two volumes.

        Args:
            volume1 (float or int): The first volume value.
            volume2 (float or int): The second volume value.

        Returns:
            tuple: A tuple containing the comparison result (-1 if v1 < v2, 0 if equal, 1 if v1 > v2) 
                   and the difference between them (v1 - v2).
        """
        # Handle potential non-numeric inputs by attempting conversion or raising an error implicitly via logic flow.
        try:
            val1 = float(volume1)
            val2 = float(volume2)
        except (TypeError, ValueError):
            raise TypeError("Both volume arguments must be numeric.")

        if val1 < val2:
            result = -1
        elif val1 > val2:
            result = 1
        else:
            result = 0
        
        difference = val1 - val2
        return (result, difference)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    comparator = VolumeComparator()

    test_cases = [
        ((50, 30), (-1, 20)),          # v1 < v2
        ((75, 75), (0, 0)),            # Equal volumes
        ((100, 40), (1, 60)),          # v1 > v2
    ]

    print("Running VolumeComparator tests...\n")
    
    for i, inputs in enumerate(test_cases):
        expected_result = inputs[0]
        
        result_tuple = comparator.compare(inputs[0][0], inputs[0][1]) if isinstance(inputs[0], tuple) else (inputs[0][0], inputs[0][1])
        
        # Adjusting input access for the test cases structure above: 
        # The loop variable 'i' is index, but we need to pass arguments correctly.
        # Let's restructure slightly for clarity in execution within this block.
        pass

    # Re-executing logic explicitly based on sample values defined directly here for maximum clarity and no ambiguity.
    
    v1_a = 50
    v2_a = 30
    
    res, diff = comparator.compare(v1_a, v2_a)
    print(f"Comparing {v1_a} vs {v2_a}: Result={res}, Difference={diff}")

    v1_b = 75.5
    v2_b = 75.5

    res, diff = comparator.compare(v1_b, v2_b)
    print(f"Comparing {v1_b} vs {v2_b}: Result={res}, Difference={diff:.4f}")

    v1_c = 100
    v2_c = 40
    
    res, diff = comparator.compare(v1_c, v2_c)
    print(f"Comparing {v1_c} vs {v2_c}: Result={res}, Difference={diff}")