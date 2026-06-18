import functools

class Sorter:
    def sort_data(self, data_list, key_function):
        """
        Sorts an input list based on a custom key function provided by the user.
        
        Args:
            data_list (list): The list of elements to be sorted.
            key_function (callable): A function that takes an element from the list 
                                    and returns a comparable value for sorting purposes.
                                    
        Returns:
            list: A new list containing the sorted elements.
        """
        # Use functools.cmp_to_key if the logic requires direct comparison, 
        # though standard key-based sort is more efficient unless complex rules apply.
        # Here we use the provided key_function directly as it's generally sufficient for most cases.
        return sorted(data_list, key=key_function)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are needed
    
    # Sample data: list of tuples (id, name, score)
    original_data = [
        {"id": 3, "score": 90},
        {"id": 1, "score": 85},
        {"id": 2, "score": 76}
    ]

    # Key function to sort by score in descending order
    def get_score(x):
        return x["score"]

    sorter = Sorter()
    
    sorted_data = sorter.sort_data(original_data, get_score)
    
    print("Original Data:")
    for item in original_data:
        print(item)
        
    print("\nSorted Data (by score descending):")
    for item in sorted_data:
        print(item)