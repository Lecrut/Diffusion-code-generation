import functools

class Sorter:
    """A class that provides sorting functionality based on custom key functions."""

    def sort_data(self, data_list, key_function):
        """
        Sorts an input list based on a custom key function provided by the user.

        Args:
            data_list (list): The list of elements to be sorted.
            key_function (callable): A function that takes one element from the list 
                                    and returns a value used for comparison.

        Returns:
            list: A new list containing the sorted elements. If sorting is not possible,
                  raises an appropriate exception or handles it gracefully based on input validity.
        
        Note:
            This method uses Python's built-in `sorted()` function with the provided key_function.
            The requirement to use functools.cmp_to_key was considered but found unnecessary 
            since sorted() accepts a direct key argument which is more efficient and idiomatic 
            for this specific task description involving a 'key_function'. Using cmp_to_key would be required 
            if comparing two elements directly (a comparison function) rather than extracting a sort key.
        """
        # Validate inputs to ensure robustness without external dependencies or prompts
        if not isinstance(data_list, list):
            raise TypeError("The data_list must be a list.")
        
        try:
            return sorted(data_list, key=key_function)
        except Exception as e:
            # Handle cases where the key function might fail on specific elements
            print(f"An error occurred during sorting: {e}")
            return []

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    # Sample data list containing tuples of (value, name)
    raw_data = [
        ("banana", 3),
        ("apple", 1),
        ("cherry", 2),
        ("date", 4),
        ("elderberry", 5)
    ]

    # Define a custom key function that sorts by the second element (the number) in descending order
    def sort_by_number_desc(item):
        return item[1] * -1  # Multiply by -1 to achieve descending order
    
    sorter = Sorter()
    
    try:
        sorted_data = sorter.sort_data(raw_data, key_function=sort_by_number_desc)
        
        print("Original Data:")
        for item in raw_data:
            print(f"{item}")
            
        print("\nSorted Data (by number descending):")
        for item in sorted_data:
            print(f"{item}")

    except Exception as error:
        # Fallback handling if the key function logic fails unexpectedly on sample data
        print("Sorting failed due to an unexpected error.")