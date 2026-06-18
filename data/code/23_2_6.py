class ValueComparator:
    """A class designed to compare two values and return a descriptive string."""

    def __init__(self):
        pass
    
    def compare(self, val1, val2):
        """
        Compares two input values of any comparable type.
        
        Args:
            val1 (any): The first value to be compared.
            val2 (any): The second value to be compared.
            
        Returns:
            str: A string indicating whether the values are greater than, 
                 less than, or equal to each other.
                 
        Raises:
            TypeError: If the input types cannot be directly compared.
        """
        # Check if comparison is supported (Python's default behavior handles most cases)
        try:
            result = val1 > val2
            
            if result:
                return f"{val1} is greater than {val2}"
            elif result == False and not isinstance(val1, type(False)):
                # Explicitly check for equality to avoid relying solely on negation of '>' 
                # which can be ambiguous with some truthy/falsy objects (though rare in this context)
                if val1 < val2:
                    return f"{val1} is less than {val2}"
                else:
                    return f"{val1} and {val2} are equal"
            elif isinstance(val1, type(False)): # Explicitly handle boolean False to avoid logic errors with > operator on booleans in some edge cases if needed, though Python's '> val1' usually works fine. 
                                     # Actually simpler: just use the standard comparison operators directly.
                return f"{val1} and {val2} are equal"

            elif result == False and not (val1 < val2):
                 return f"{val1} is less than or equal to {val2}" if val1 != val2 else f"{val1} and {val2} are equal"

        except TypeError:
            raise TypeError(f"The types of the input values cannot be compared ({type(val1).__name__}, {type(val2).__name__}).")

def main():
    """Main execution block with hard-coded sample tests."""
    
    comparator = ValueComparator()
    
    # Test case 1: Integers (val1 > val2)
    result_ints = comparator.compare(10, 5)
    print(f"Test Case 1 (Integers): {result_ints}")
    
    # Test case 2: Floats (val1 < val2)
    result_floats = comparator.compare(3.14, 2.71)
    print(f"Test Case 2 (Floats - val1 > val2): {result_floats}")

    # Note: Reordering to ensure Test case logic matches description above
    
    # Correcting the order for clarity in the sample output based on logic flow
    result_equal = comparator.compare(5, 5)
    print(f"Test Case Equal (Integers): {result_equal}")

if __name__ == '__main__':
    main()