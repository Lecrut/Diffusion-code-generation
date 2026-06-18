class ComparisonUtils:
    @classmethod
    def check_if_greater(cls, a, b):
        """
        Compares two objects of equal type to determine if 'a' is strictly greater than 'b'.
        
        Args:
            a (Comparable): The first object to compare.
            b (Comparable): The second object to compare. Must be the same type as 'a'.
            
        Returns:
            bool: True if 'a' > 'b', False otherwise.
            
        Raises:
            TypeError: If types of 'a' and 'b' are different or they do not support comparison.
        """
        if not isinstance(a, type(b)):
            raise TypeError(f"Cannot compare {type(a).__name__} with {type(b).__name__}")
        
        try:
            return a > b
        except TypeError:
            # Fallback for objects that define __lt__/__gt__ but comparison fails (e.g., custom classes)
            return False

if __name__ == '__main__':
    utils = ComparisonUtils()

    sample_values_ints = 10, 25
    
    result_integers = utils.check_if_greater(sample_values_ints[0], sample_values_ints[1])
    
    print(f"Comparison ({sample_values_ints[0]}, {sample_values_ints[1]}): {result_integers}")

    sample_values_strings = "apple", "banana"
    
    result_strings = utils.check_if_greater(sample_values_strings[0], sample_values_strings[1])
    
    print(f"Comparison ('{sample_values_strings[0]}', '{sample_values_strings[1]}'): {result_strings}")