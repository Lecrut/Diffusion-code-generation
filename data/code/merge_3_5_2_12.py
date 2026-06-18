class LengthComparator:
    def compare(self, length_a, length_b):
        """
        Compares two lengths and returns a descriptive string indicating their relationship.
        
        Parameters:
            length_a (int or float): The first length value.
            length_b (int or float): The second length value.
            
        Returns:
            str: A description of the comparison result.
        """
        if length_a > length_b:
            return f"{length_a} is greater than {length_b}"
        elif length_a < length_b:
            return f"{length_a} is less than {length_b}"
        else:
            return f"{length_a} is equal to {length_b}"

if __name__ == '__main__':
    # Sample test cases without any user input or external dependencies
    comparator = LengthComparator()

    results = [
        (10, 5),
        (3.5, 7.2),
        (4, 4),
        (-2, -8)
    ]

    for val_a, val_b in results:
        output = comparator.compare(val_a, val_b)
        print(f"Comparing {val_a} and {val_b}: '{output}'")