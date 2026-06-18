class WeightCalculator:
    """A class to calculate differences between weights."""

    def difference(self, weight1: float, weight2: float) -> float:
        """Calculate the absolute difference between two weights.
        
        Args:
            weight1: The first weight value (float).
            weight2: The second weight value (float).
            
        Returns:
            The absolute difference between the two weights as a float.
        """
        return abs(weight1 - weight2)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    calc = WeightCalculator()

    # Sample inputs: 50.5 kg and 48.7 kg
    val_a = 50.5
    val_b = 48.7
    
    result = calc.difference(val_a, val_b)
    
    print(f"Difference between {val_a} kg and {val_b} kg is: {result:.2f}")