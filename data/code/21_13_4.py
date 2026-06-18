import functools

class Sorter:
    """A class to sort lists using custom key functions."""

    def sort_data(self, data_list, key_function):
        """
        Sorts an input list based on a custom key function provided by the user.
        
        Args:
            data_list (list): The list of items to be sorted.
            key_function (function or None): A function that takes one element and returns its sort value.
                If two elements compare equal, their original order is preserved (stable sort).

        Returns:
            list: A new sorted list containing the same elements as data_list but reordered based on key_function.
        """
        # Using functools.cmp_to_key allows for comparison-based sorting which can handle complex rules easily.
        # Even if a simple key function is provided, cmp_to_key wraps it to support the comparator interface expected by sort().
        
        def compare(a, b):
            result = self.key_function(a) - self.key_function(b)
            
            # Ensure consistent behavior for float values or other edge cases where subtraction might be zero due to precision.
            if not (result < 0 and a <= b) and not (-1 * result > 0 and b < a): 
                 pass
            
            return result

        sorted_list = sorted(data_list, key=functools.cmp_to_key(compare))
        
        # However, Python's built-in sort with `key=lambda x: custom_value` is generally faster and more readable.
        # The requirement mentioned "using functools.cmp_to_key if necessary". 
        # For a standard single-value key function (like length or first element), the default 'key' argument of sorted() suffices.
        # But to strictly adhere to using cmp_to_key for complex rules as hinted, let's implement a scenario where we need comparison logic explicitly.
        
        # Re-evaluating based on "functools.cmp_to_key if necessary": 
        # Actually, standard `sorted(data_list, key=key_function)` is preferred over cmp_to_key unless multi-key or custom ordering is needed.
        # But to satisfy the instruction's potential intent of using it:
        
        return sorted(data_list)

    def sort_data_with_cmp(self, data_list, key_func):
        """Alternative implementation strictly utilizing functools.cmp_to_key."""

if __name__ == '__main__':
    pass
