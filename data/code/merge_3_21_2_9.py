class Sorter:
    """A utility class to sort lists of numbers."""

    def sort_list(self, data_list):
        """
        Sorts a list of numbers in reverse (descending) order.

        Args:
            data_list (list): A list containing numeric values.

        Returns:
            list: The sorted list in descending order.
        """
        return sorted(data_list, reverse=True)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    sample_data = [5, 2, 9, 1, 7, 3]

    sorter_instance = Sorter()
    sorted_result = sorter_instance.sort_list(sample_data)

    print("Original list:", sample_data)
    print("Sorted (descending):", sorted_result)