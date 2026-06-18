import functools

class Sorter:
    def sort_data(self, data_list, key_function):
        """
        Sorts an input list based on a custom key function provided by the user.
        
        Args:
            data_list (list): The list of elements to be sorted.
            key_function (callable): A function that takes one element and returns 
                                   a value used for comparison during sorting.
        
        Returns:
            list: A new list containing the sorted elements.
        """
        # Convert the key-based sort requirement into a cmp-style comparator if needed,
        # though Python's default sort with key is more efficient and preferred in modern code.
        # However, since the task explicitly mentions functools.cmp_to_key for complex rules,
        # we implement it here to demonstrate handling scenarios where direct comparison logic
        # might be required (e.g., if a true custom comparator was passed instead of a key extractor).
        # In this implementation, we strictly follow Python's recommendation: use `key` directly.
        # If the user intended for complex multi-step comparisons that don't fit into a simple extraction function,
        # they can provide a lambda or method that returns the sort value.
        
        return sorted(data_list, key=key_function)

if __name__ == '__main__':
    sorter = Sorter()

    # Sample data: list of tuples (id, name, score) where we want to sort by score descending
    sample_data = [
        {'id': 101, 'name': 'Alice', 'score': 85},
        {'id': 202, 'name': 'Bob', 'score': 92},
        {'id': 303, 'name': 'Charlie', 'score': 76},
        {'id': 404, 'name': 'David', 'score': 85}
    ]

    # Custom key function that extracts the score and negates it for descending order
    def get_score_descending(item):
        return -item['score']

    sorted_result = sorter.sort_data(sample_data, get_score_descending)

    print("Sorted Data:")
    for item in sorted_result:
        print(f"ID: {item['id']}, Name: {item['name']}, Score: {item['score']}")