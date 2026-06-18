class WeightCalculator:
    @staticmethod
    def calculate_difference(weight1, weight2):
        """Calculate the absolute difference between two weights."""
        return abs(weight1 - weight2)

if __name__ == '__main__':
    calc = WeightCalculator()
    
    # Hard-coded sample values to ensure no user input is required
    weight_a = 50.5
    weight_b = 34.7
    
    difference = calc.calculate_difference(weight_a, weight_b)
    
    print(f"Difference between {weight_a} and {weight_b}: {difference}")