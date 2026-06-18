class Sorter:
    """A class providing utility methods to sort lists of numbers."""

    def sort_list(self, data_list):
        """Sorts a list of numbers in reverse (descending) order and returns it.

        Args:
            data_list (list): A list containing numerical values.

        Returns:
            list: The sorted list in descending order.
        
        Raises:
            TypeError: If the input is not a list or contains non-numeric elements.
        """
        if not isinstance(data_list, list):
            raise TypeError(f"Expected a list, got {type(data_list).__name__}")

        for item in data_list:
            if not isinstance(item, (int, float)):
                raise TypeError("List must contain only numeric values.")

        return sorted(data_list, reverse=True)

if __name__ == '__main__':
    sample_data = [64, 34, 25, 12, 98, 76]
    sorter_instance = Sorter()
    result = sorter_instance.sort_list(sample_data)
    print(result)