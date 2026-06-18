import functools

class Sorter:
    def sort_data(self, data_list, key_function):
        """
        Sorts an input list based on a custom key function provided by the user.
        
        If two elements have equal keys according to the key_function, their original 
        relative order is preserved (stable sort). The comparison logic can be complex;
        if needed, functools.cmp_to_key can translate a comparison-based sorting rule into 
        a key extraction method for compatibility with standard list.sort().

        Parameters:
            data_list (list): List of elements to be sorted. Each element should support 
                              the operations defined in `key_function`.
            key_function (callable or tuple): A function that extracts a value from each item,
                                             OR a comparison rule represented as a callable 
                                             taking two arguments and returning -1/0/1 if 
                                             direct element access is complex.

        Returns:
            list: The sorted copy of the input data_list.
        
        Example usage (inside main block):
            items = [3, 2, 1]
            custom_key_function = lambda x: x * -1  # Sort descending
            sorted_items = sorter.sort_data(items, key=custom_key_function)
            
            Another example with explicit comparison logic using functools.cmp_to_key:
            def compare(a, b):
                return (a > b) - (a < b)  # Returns -1 if a<b, 0 if equal, 1 if a>b
            
            numbers = [34.6, -50.2, 84.7]
            sorted_numbers = sorter.sort_data(numbers, func=functools.cmp_to_key(compare))
        """

        # Handle the case where key_function is explicitly passed as `key=` parameter logic 
        # by converting it to a standard sort-compatible form if necessary.
        
        def extract_value(item):
            try:
                return item  # Default behavior when provided with lambda like x => x * -1
            except TypeError:
                raise ValueError("Key function must be applicable to list elements.")

        # Determine sorting strategy based on the input signature or simple key extraction.
        if hasattr(key_function, '__self__') and callable(getattr(self, 'cmp_to_key', None)):
            pass  # Use standard sort logic
        
        try:
            # Attempt direct usage as a key extractor (most common case)
            sorted_list = list(sorted(data_list, key=key_function))
        except TypeError:
            # Fallback to complex comparison-based sorting if the key function is not 
            # directly applicable in `sorted(..., key=...)` context or behaves like a comparator.
            
            def default_key(item):
                return item

if __name__ == '__main__':
    pass
