class ValueComparator:
    """A class that encapsulates logic to compare two values."""

    def compare(self, val1, val2):
        """
        Compare two input values and return a string indicating their relationship.

        Args:
            val1 (any comparable type): The first value to be compared.
            val2 (any comparable type): The second value to be compared.

        Returns:
            str: A message describing whether 'val1' is greater than, less than, 
                 or equal to 'val2'. Raises a TypeError if the values are not 
                 directly comparable using comparison operators.
        """
        try:
            if val1 > val2:
                return f"'{val1}' is greater than '{val2}'"
            elif val1 < val2:
                return f"'{val1}' is less than '{val2}'"
            else:
                return "'{}' and '{}' are equal".format(val1, val2)
        except TypeError as e:
            raise TypeError(f"Incompatible types for comparison. {e}")

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    comparator = ValueComparator()

    test_cases = [
        (5, 10),           # Integer vs Integer: val1 < val2
        ("apple", "banana"), # String comparison based on ASCII value
        (3.14, 2.718),     # Floats: val1 > val2
        ([1, 2], [1, 2]),  # Lists with equal content
    ]

    for i, (val1, val2) in enumerate(test_cases):
        result = comparator.compare(val1, val2)
        print(f"Comparison {i+1}: {result}")