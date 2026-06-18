class Sorter:
    """A class that provides sorting functionality for lists of numbers."""

    def sort_list(self, data_list):
        """Sorts a list of numbers in reverse (descending) order and returns it.

        Args:
            data_list (list): A list containing numerical values to be sorted.

        Returns:
            list: The same list object with elements reordered in descending order.

        Raises:
            TypeError: If the input is not a list or contains non-numeric types.
        """
        if not isinstance(data_list, list):
            raise TypeError("Input must be a list.")

        for item in data_list:
            if not isinstance(item, (int, float)):
                raise TypeError(f"List contains invalid type {type(item).__name__}. Only numbers are allowed.")

        return sorted(data_list, reverse=True)

if __name__ == '__main__':
    # Sample test case with hard-coded values. No user input or external dependencies required.
    sample_data = [34, 7, 23, 10, 99, 5]

    sorter_instance = Sorter()
    sorted_result = sorter_instance.sort_list(sample_data)

    print("Original list:", sample_data)
    print("Sorted (descending):", sorted_result)