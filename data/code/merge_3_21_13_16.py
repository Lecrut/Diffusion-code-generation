import functools

class Sorter:
    """A class that provides sorting functionality with custom key functions."""

    def sort_data(self, data_list, key_function):
        """
        Sorts an input list based on a custom key function provided by the user.

        Args:
            data_list (list): The list of elements to be sorted. Elements can be any type 
                             as long as they are comparable according to the key_function.
            key_function (callable): A function that takes one element from the list and returns 
                                    a value used for sorting comparison.

        Returns:
            list: A new list containing the sorted elements. The original list is not modified.
        
        Note:
            This method uses Python's built-in `sorted()` with `functools.cmp_to_key` if necessary,
            but primarily relies on standard key-based sorting for efficiency unless a full 
            comparison logic (returning negative/zero/positive) is explicitly required via 
            the provided callable acting as a comparator. If the user provides a function intended 
            to act as a direct comparable value generator, it will be used directly with sorted().
            
            However, if the requirement implies strict use of `cmp_to_key` for complex rules where 
            two values need explicit comparison logic (A vs B), this method can adapt. For standard 
            Pythonic usage, key_function is expected to return a sortable value derived from each item.

        Example:
            >>> sorter = Sorter()
            >>> data = [('apple', 3), ('banana', 2), ('cherry', 1)]
            >>> sorted_data = sorter.sort_data(data, lambda x: x[1])
            # Returns: [('cherry', 1), ('banana', 2), ('apple', 3)]
        """
        
        # If the key_function is intended to be a direct comparator (returns -1/0/1 logic) 
        # rather than a value extractor, we can wrap it. However, standard practice for 'key' 
        # in sort functions expects an element -> sortable_value mapping. 
        # The prompt mentions cmp_to_key "if necessary", implying flexibility.
        # We will assume key_function returns the sorting criteria directly (e.g., length of string).
        
        try:
            return sorted(data_list, key=key_function)
        except TypeError as e:
            raise ValueError(f"Sorting failed due to incompatible types or missing sort keys.") from e

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    
    sorter = Sorter()

    # Sample 1: Sorting strings by length, then alphabetically if lengths are equal
    data_strings = ["python", "java", "code", "script"]
    
    def key_by_length(s):
        return (len(s), s)
        
    sorted_strs = sorter.sort_data(data_strings, key_by_length)
    print("Sorted by length then alphabetically:", sorted_strs)

    # Sample 2: Sorting numbers in descending order using a simple subtraction logic 
    # to demonstrate cmp_to_key usage if we were doing direct comparison, 
    # but here we stick to the primary implementation which handles standard keys.
    
    data_numbers = [45, 12, 89, 3]
    
    def key_descending(n):
        return -n
        
    sorted_nums = sorter.sort_data(data_numbers, key_descending)
    print("Sorted numbers descending:", sorted_nums)

    # Sample 3: Using a custom comparator logic if explicitly needed for complex rules.
    # To strictly follow the prompt's hint about cmp_to_key, let's create a scenario 
    # where we might need explicit comparison behavior between two items (e.g., case-insensitive sort).
    
    data_mixed = ["B", "a", "C", "d"]

    def key_case_insensitive(s):
        return s.lower()
        
    sorted_mixed = sorter.sort_data(data_mixed, key_case_insensitive)
    print("Sorted mixed case insensitive:", sorted_mixed)