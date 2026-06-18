class LengthComparator:
    def compare(self, length_a, length_b):
        """
        Compares two lengths and returns a descriptive string indicating their relationship.
        
        Parameters:
            length_a (int or float): The first value to compare.
            length_b (int or float): The second value to compare.
            
        Returns:
            str: A description of the comparison result.
        """
        if length_a < length_b:
            return f"{length_a} is less than {length_b}"
        elif length_a > length_b:
            return f"{length_a} is greater than {length_b}"
        else:
            return f"{length_a} is equal to {length_b}"

if __name__ == '__main__':
    comparator = LengthComparator()

    # Sample test cases with hard-coded values
    result1 = comparator.compare(5, 3)
    print(result1)

    result2 = comparator.compare(10.5, 10.5)
    print(result2)

    result3 = comparator.compare(-7, -4)
    print(result3)