class ValueComparator:
    """A class to compare two input values."""

    def compare(self, val1, val2):
        """
        Compare two values and return a string indicating their relationship.

        Args:
            val1 (Any): The first value to compare.
            val2 (Any): The second value to compare.

        Returns:
            str: A message describing whether val1 is greater than, less than, or equal to val2.
        """
        if val1 > val2:
            return "val1 is greater"
        elif val1 < val2:
            return "val1 is smaller"
        else:
            return "values are equal"

if __name__ == '__main__':
    # Sample test cases running without user input or external dependencies
    comparator = ValueComparator()

    print(comparator.compare(5, 3))   # Output: val1 is greater
    print(comparator.compare("apple", "banana"))  # Output: val1 is smaller (alphabetical)
    print(comparator.compare([1, 2], [1]))      # Output: val1 is greater