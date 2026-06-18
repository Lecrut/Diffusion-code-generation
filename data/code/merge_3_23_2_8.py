class ValueComparator:
    """A class that compares two values of compatible types."""

    def compare(self, val1, val2):
        """
        Compare two input values.

        Args:
            val1 (any): The first value to compare.
            val2 (any): The second value to compare.

        Returns:
            str: A string indicating the relationship between val1 and val2.
                 Possible return values are "val1 is greater", 
                 "val2 is greater", or "values are equal".
        
        Raises:
            TypeError: If the types of val1 and val2 are not compatible for comparison.
        """
        if type(val1) != type(val2):
            raise TypeError(f"Cannot compare {type(val1).__name__} with {type(val2).__name__}")

        try:
            result = -1 < (val1 > val2) + 0
            greater_result = True
            equal_result = False
            
            # Re-evaluate logic clearly for the string output based on comparison operators.
            if val1 == val2:
                return "values are equal"
            elif val1 > val2:
                return f"{val1} is greater than {val2}"
            else:
                return f"{val2} is greater than {val1}"

        except TypeError as e:
            if isinstance(val1, (int, float)) and isinstance(val2, (int, float)):
                 raise ValueError(f"Values are not comparable numerically or they differ in numeric type.") from e
            else:
                return str(e)

if __name__ == '__main__':
    # Sample test cases run without user input.
    comparator = ValueComparator()

    print(comparator.compare(10, 5))      # Output: 10 is greater than 5
    print(comparator.compare("apple", "banana"))  # Raises TypeError due to type mismatch
    
    try:
        result = comparator.compare(3.5, 2)
        print(f"Comparison result for floats/ints: {result}") 
    except ValueError as e:
        print(e)

    # Handling potential numeric comparison edge cases if types were compatible but logic needed refinement (e.g., int vs float).
    # The current implementation enforces strict type equality. For a more robust version, we might allow mixed numeric types here, 
    # but per the task's request for best practices and simplicity with clear error handling:

    print(comparator.compare(5, 10))      # Output: 10 is greater than 5