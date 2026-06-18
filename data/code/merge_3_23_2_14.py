class ValueComparator:
    """A class that compares two values of various types."""
    
    def __init__(self):
        self.comparisons = []

    def compare(self, val1, val2):
        """
        Compares two input values and returns a string indicating 
        which value is greater, less, or if they are equal.

        Args:
            val1 (any): The first value to compare.
            val2 (any): The second value to compare.

        Returns:
            str: A message describing the comparison result ('val1 > val2', 'val1 < val2', 
                 or 'val1 == val2'). Prints a debug statement with both values and their types,
                 then returns the formatted string without newlines (except at end).
        """

        self.comparisons.append((type(val1).__name__, type(val2).__name__))
        
        result = ""

        try:
            if val1 > val2:
                result = f"{val1} is greater than {val2}"
            elif val1 < val2:
                result = f"{val1} is less than {val2}"
            else:
                result = f"{val1} and {val2} are equal"

        except TypeError as e:
            if "unorderable types:" in str(e):
                return f"Incompatible comparison type ({type(val1).__name__}, {type(val2).__name__}). Cannot compare."
            else:
                raise

        print(f"{val1} ({type(val1).__name__}) and {val2} ({type(val2).__name__}): " + result)
        
        return result

if __name__ == '__main__':
    comp = ValueComparator()
    
    # Sample 1: Integer comparison - val1 > val2
    res1 = comp.compare(10, 5)

    # Sample 2: Float comparison - val1 < val2  
    res2 = comp.compare(3.14, 99.99)

    # Sample 3: String comparison (lexicographical) - equal
    res3 = comp.compare("hello", "world")
    
    print(res1 + "\n" + res2 + "\n" + res3)