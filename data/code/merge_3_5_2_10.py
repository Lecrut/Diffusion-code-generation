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
    # Sample test cases with hard-coded values, no user input required.
    comparator = LengthComparator()

    results = [
        (10, 5),      # length_a > length_b
        (7, 7),       # equal
        (3.5, 4.2),   # float comparison: less than
        (-2, -8),     # negative numbers: greater than
    ]

    for a, b in results:
        output = comparator.compare(a, b)
        print(f"Comparing {a} and {b}: '{output}'")