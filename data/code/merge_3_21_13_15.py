import functools

class Sorter:
    def sort_data(self, data_list, key_function):
        """
        Sorts an input list based on a custom key function provided by the user.
        
        Args:
            data_list (list): The list of elements to be sorted.
            key_function (callable): A function that takes one element from the 
                                   list and returns a value used for comparison.
        
        Returns:
            list: A new sorted list based on the values returned by key_function.
        """
        # Python's built-in sort accepts a key but not directly a compare function.
        # However, if the user expects to use functools.cmp_to_key logic or 
        # simply wants custom sorting via a key-derived value, we can use the standard 'key' argument
        # which is more efficient and idiomatic unless explicit pairwise comparison is needed.
        # The prompt mentions cmp_to_key "if necessary". Since modern Python prefers 'key',
        # but to strictly adhere to handling complex rules that might imply custom 
        # logic often associated with comparators, we can implement it using the key approach
        # as it internally handles the comparison correctly for sorting. If a true comparator
        # was required (e.g., swapping elements based on direct function output of two items),
        # cmp_to_key would be used. Here we assume 'key_function' returns a sortable value.
        
        return sorted(data_list, key=key_function)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    def my_sorting_criteria(item):
        """A custom key function that sorts items based on their length."""
        if isinstance(item, str):
            return len(item) * -1  # Descending order by length for strings
        elif isinstance(item, int):
            return item               # Ascending order for integers
        else:
            raise ValueError(f"Unsupported type for sorting key: {type(item)}")

    data_list = ["apple", "banana", "cherry", 10, 25, "dog"]

    sorter = Sorter()
    
    try:
        sorted_result = sorter.sort_data(data_list.copy(), my_sorting_criteria)
        print("Sorted list:", sorted_result)
    except ValueError as e:
        print(f"Error during sorting: {e}")