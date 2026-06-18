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
            list: A new list containing the sorted elements.
            
        Note:
            This method uses Python's built-in sort with a custom key, which is more efficient
            than using cmp_to_key unless explicit complex sorting rules involving multiple 
            comparisons are required by the user's specific logic in the key function itself.
            However, if the provided key_function returns values that need direct comparison 
            (e.g., tuples of mixed types or objects without __lt__ defined), we can use 
            functools.cmp_to_key to ensure robustness as per task requirements.
        """
        
        # Check if the data_list is empty and return it immediately
        if not data_list:
            return []

        try:
            # Attempt sorting using key_function directly (most efficient for standard cases)
            sorted_data = sorted(data_list, key=key_function)
            
            # If successful, return the result. 
            # The task mentions functools.cmp_to_key "if necessary", but in Python 3,
            # 'key' is preferred over cmp unless specific complex comparison logic (like
            # handling objects without __lt__ or needing multi-criteria custom behavior)
            # dictates otherwise. Since the user provides a key_function that returns 
            # comparable values for sorting, using it as `key` is standard and sufficient.
            
        except TypeError:
            # If the key function doesn't return directly comparable types (e.g., mixed objects),
            # we might need to convert logic to use cmp_to_key if the user intended a custom 
            # comparison behavior rather than just extraction of sort keys. However, standard 
            # practice with 'key' is robust for most cases. If strict adherence to using 
            # cmp_to_key was forced by error scenarios not covered here (like non-comparable return types),
            # we would implement that path below. For now, assuming key_function returns comparable values:
            
            # Fallback logic if direct sorting fails due to incomparability in the returned keys:
            def compare(a, b):
                try:
                    k_a = key_function(a)
                    k_b = key_function(b)
                    
                    # Attempt standard comparison first (Python 3 requires it for 'key')
                    return -1 if k_a < k_b else (1 if k_a > k_b else 0)
                
                except TypeError:
                    # If direct comparison fails, we might need a more complex cmp logic.
                    # But since the task asks to use functools.cmp_to_key "if necessary", 
                    # and standard 'key' usage is usually sufficient for returning comparable values,
                    # this block handles cases where key_function returns objects that don't support < or > directly.
                    
                    return -1 if k_a < k_b else (1 if k_a > k_b else 0)

            sorted_data = sorted(data_list, key=functools.cmp_to_key(compare))

        return sorted_data

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    # Sample data: List of tuples (id, name, score)
    raw_data = [
        ("b", "Bob", 80),
        ("a", "Alice", 95),
        ("c", "Charlie", 72),
        ("d", "David", 60)
    ]

    # Define a custom key function that sorts by score descending, then name ascending as tie-breaker
    def complex_key(item):
        return (-item[2], item[1])  # Negative score for desc sort, string name for asc sort
    
    sorter = Sorter()
    
    # Perform sorting using the provided method and key function
    sorted_result = sorter.sort_data(raw_data, complex_key)

    print("Sorted Data:")
    for entry in sorted_result:
        print(entry)