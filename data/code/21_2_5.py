class Sorter:
    """A class providing sorting utilities."""

    def sort_list(self, data_list):
        """Sorts a list of numbers in reverse (descending) order.

        Args:
            data_list (list): A list containing numerical values to be sorted.

        Returns:
            list: The same list object now sorted in descending order.
        """
        return sorted(data_list, reverse=True)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    sample_data = [5, 2, 89, -3, 10]

    sorter_instance = Sorter()
    result = sorter_instance.sort_list(sample_data)

    print("Sorted list (descending):", result)