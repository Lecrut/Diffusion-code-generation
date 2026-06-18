class WeightCalculator:
    """A class to calculate differences between two weights."""

    def difference(self, weight1: float, weight2: float) -> float:
        """Calculate the absolute difference between two weights.
        
        Args:
            weight1 (float): The first weight value.
            weight2 (float): The second weight value.
            
        Returns:
            float: The absolute difference between weight1 and weight2.
        """
        return abs(weight1 - weight2)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    calc = WeightCalculator()

    w_a = 50.5
    w_b = 48.2

    result = calc.difference(w_a, w_b)

    print(f"Difference between {w_a} and {w_b}: {result}")