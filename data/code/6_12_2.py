class WeightCalculator:
    """A class to handle weight calculations."""

    def calculate_difference(self, weight1: float, weight2: float) -> float:
        """Calculate the absolute difference between two weights.
        
        Args:
            weight1 (float): The first weight value.
            weight2 (float): The second weight value.
            
        Returns:
            float: The absolute difference between the two weights.
            
        Raises:
            TypeError: If either input is not a number.
            ValueError: If inputs are NaN or infinite values, which don't make sense for physical weight.
        """
        if not isinstance(weight1, (int, float)) or not isinstance(weight2, (int, float)):
            raise TypeError("Both weights must be numbers.")
        
        import math
        
        # Check for invalid numerical inputs
        if not math.isfinite(weight1) or not math.isfinite(weight2):
            raise ValueError("Weights must be finite real numbers.")

        return abs(weight1 - weight2)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    
    calculator = WeightCalculator()

    # Sample 1: Standard positive weights (e.g., in kilograms or pounds, scale doesn't matter for diff)
    w_a = 50.0
    w_b = 30.0
    
    try:
        result_1 = calculator.calculate_difference(w_a, w_b)
        print(f"Difference between {w_a} and {w_b}: {result_1}")
        
        # Sample 2: Integer weights to show type handling works for int too
        c = 80
        d = 45
        
        result_2 = calculator.calculate_difference(c, d)
        print(f"Difference between {c} and {d}: {result_2}")

    except (TypeError, ValueError) as e:
        # In a real scenario with user input we would handle this differently, 
        # but here the hard-coded values are valid so exceptions won't trigger.
        pass
        
    print("All calculations completed successfully.")