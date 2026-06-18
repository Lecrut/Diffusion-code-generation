class Sorter:
    """A utility class to sort lists of numbers."""

    def sort_list(self, data_list):
        """
        Sorts a list of numbers in reverse (descending) order and returns it.
        
        This method modifies the input list in-place if sorting is performed 
        via .sort(), or could return a new sorted list depending on design choice.
        Here we choose to sort in-place for efficiency, as per typical best practices
        when mutable lists are passed unless specified otherwise (copy-on-write).

        Parameters:
            data_list (list): A list of numeric values to be sorted.

        Returns:
            The same list object now sorted in descending order.
        
        Example:
            >>> sorter = Sorter()
            >>> numbers = [3, 1, 4]
            >>> result = sorter.sort_list(numbers)
            >>> print(result)
            [4, 3, 1]
        """
        # Ensure the list is a list type to avoid errors with tuples or other iterables
        data_list = list(data_list) 
        # Sort in reverse order (descending)
        data_list.sort(reverse=True)
        return data_list

if __name__ == '__main__':
    sample_data = [65, 34, 89, 12, 77]

    sorter = Sorter()
    sorted_result = sorter.sort_list(sample_data)

    print("Original list:", sample_data)
    print("Sorted (descending):", sorted_result)