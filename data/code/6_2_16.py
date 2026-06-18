class WeightCalculator:
    """A class to perform basic weight calculations."""

    def calculate_difference(self, weight1, weight2):
        """Calculate the difference between two weights.
        
        Args:
            weight1 (float or int): The first weight value.
            weight2 (float or int): The second weight value.
            
        Returns:
            float: The absolute difference between the two weights.
        """
        return abs(weight1 - weight2)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    calc = WeightCalculator()

    w_a = 50.5
    w_b = 30.2

    diff = calc.calculate_difference(w_a, w_b)

    print(f"The difference between {w_a} and {w_b} is: {diff}")