class Sorter:
    """A utility class to sort lists of numbers."""

    def sort_list(self, data_list):
        """
        Sorts a list of numbers in descending (reverse) order.

        Parameters:
            data_list (list): A list containing numeric values to be sorted.

        Returns:
            list: A new list with the elements sorted in reverse order.
        
        Note:
            The method creates and returns a copy of the input list, 
            avoiding side effects on the original data structure.
            
        Example:
            >>> sorter = Sorter()
            >>> result = sorter.sort_list([3, 1, 2])
            >>> print(result)
            [3, 2, 1]
        """
        return sorted(data_list, reverse=True)

if __name__ == '__main__':
    # Hard-coded sample values for demonstration purposes.
    sample_numbers = [45, 12, 89, 30, 67, 23, 99]

    sorter = Sorter()
    sorted_result = sorter.sort_list(sample_numbers)

    print("Original list:", sample_numbers)
    print("Sorted (descending):", sorted_result)