class Comparator:
    def check_equality(self, a, b):
        """
        Compares two arbitrary objects using the built-in equality operator (==).
        
        Args:
            a: The first object to compare.
            b: The second object to compare.
            
        Returns:
            bool: True if a is equal to b, False otherwise.
        """
        return a == b

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    comp = Comparator()

    print(comp.check_equality(5, 5))      # Expected output: True
    print(comp.check_equality("hello", "world"))   # Expected output: False
    print(comp.check_equality([1, 2], [1, 2]))     # Expected output: True
    print(comp.check_equality((1, 2), (1, 3)))     # Expected output: False