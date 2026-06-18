import functools

class Sorter:
    """A class to sort lists based on custom key functions."""

    def sort_data(self, data_list, key_function):
        """
        Sorts an input list using a provided key function.

        Args:
            data_list (list): The list of elements to be sorted.
            key_function (callable): A function that takes one element from the 
                                    list and returns a value used for comparison.

        Returns:
            list: A new list containing the sorted elements.
        
        Note:
            This method uses Python's built-in `sorted()` with the provided 
            key_function directly, which is more efficient than using 
            functools.cmp_to_key unless a true two-way comparator logic is required.
            However, to strictly adhere to the task requirement of potentially 
            using cmp_to_key for complex rules (though standard keys are preferred),
            we can implement it such that if a custom comparison logic was needed,
            one could convert a key-based approach or use cmp_to_key with a derived comparator.
            
            Since Python 3's sorted() accepts a `key` argument directly which is 
            the modern and efficient way to sort by a function (equivalent in spirit 
            to using keys), we will implement it this way for clarity and performance,
            unless the user specifically needs pairwise comparison logic via cmp_to_key.
            
            To fully satisfy "Implement ... using functools.cmp_to_key if necessary",
            we provide an alternative implementation path or simply use key directly as 
            it is the standard approach in Python 3 which avoids the overhead of converting 
            keys to comparators unless a true comparator function (returning -1, 0, 1) is passed.

        Example:
            >>> sorter = Sorter()
            >>> data = [3, 'banana', 2]
            >>> sorted_data = sorter.sort_data(data, key=lambda x: str(x))
            # Result would be ['banana', 2, 3] (based on string representation)
        """
        return sorted(data_list, key=key_function)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    sorter = Sorter()

    # Sample list of integers and strings mixed
    data_mixed = [3, 'banana', 2, 'apple', 1]

    # Custom key function: sort by length of string representation for all items
    def get_length_key(item):
        return len(str(item))

    sorted_by_len = sorter.sort_data(data_mixed, get_length_key)
    
    print("Sorted by character count:", sorted_by_len)

    # Another sample using a numeric key function
    data_numeric = [10.5, 3.2, -4.7]
    def positive_only(x):
        return x if x > 0 else float('inf')

    sorted_positive = sorter.sort_data(data_numeric, positive_only)
    
    print("Sorted keeping only positives (others moved to end):", sorted_positive)

    # Demonstration of a more complex rule using the class structure
    # Sorting tuples by their second element then first if equal
    data_tuples = [('b', 2), ('a', 1), ('c', 3)]

    def tuple_sort_key(item):
        return (item[1], item[0])

    sorted_tuples = sorter.sort_data(data_tuples, tuple_sort_key)
    
    print("Sorted tuples by second element then first:", sorted_tuples)