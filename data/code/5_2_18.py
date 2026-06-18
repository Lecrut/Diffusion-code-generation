class LengthComparator:
    def compare(self, length_a, length_b):
        """
        Compares two lengths and returns a descriptive string indicating their relationship.
        
        Args:
            length_a (int or float): The first length value.
            length_b (int or float): The second length value.
            
        Returns:
            str: A description of the comparison result.
        """
        if length_a == length_b:
            return f"{length_a} is equal to {length_b}"
        elif length_a > length_b:
            return f"{length_a} is greater than {length_b}"
        else:
            return f"{length_a} is less than {length_b}"

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    comparator = LengthComparator()
    
    test_cases = [
        (10, 5),      # length_a > length_b
        (7.5, 3.2),   # float comparison, length_a > length_b
        (4, 4),       # equal values
        (-2, -8),     # negative numbers, length_a > length_b
    ]
    
    for a, b in test_cases:
        result = comparator.compare(a, b)
        print(f"Comparing {a} and {b}: '{result}'")