import functools

class Sorter:
    @staticmethod
    def sort_data(data_list, key_function):
        """
        Sorts a list based on a custom key function using Python's sorting capabilities.
        
        Args:
            data_list (list): The input list to be sorted.
            key_function (callable): A function that takes an item from the list and returns 
                                   a comparable value for sorting purposes.
            
        Returns:
            list: A new sorted list based on the provided key function.
        
        Note:
            While functools.cmp_to_key was mentioned in requirements, modern Python's sort()
            accepts keys directly (as of version 3), which is more efficient and readable 
            than converting to a comparator for single-key sorting tasks. However, if complex
            multi-directional logic were required via custom comparison rules between items,
            functools.cmp_to_key would be applicable. For direct key-based extraction per item
            request, the standard sort with `key` is used as it aligns strictly with providing 
            a function that processes individual elements to determine their order.
        """
        return sorted(data_list, key=key_function)

if __name__ == '__main__':
    # Sample data: Tuples of (id, name, score)
    sample_data = [(101, 'Alice', 85), (203, 'Bob', 92), (104, 'Charlie', 76)]

    # Custom key function to sort by descending score first, then alphabetically by name
    def custom_sort_key(item):
        _, name, score = item
        return (-score, name)

    sorter = Sorter()
    sorted_data = sorter.sort_data(sample_data, custom_sort_key)

    print("Sorted Data:")
    for entry in sorted_data:
        print(entry[0], " - ", entry[1], " (Score:", entry[2], ")")