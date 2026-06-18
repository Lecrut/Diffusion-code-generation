class Sorter:
    """A class to handle sorting operations on lists of numbers."""

    def sort_list(self, data_list):
        """Sorts a list of numbers in reverse (descending) order.
        
        Args:
            data_list (list): A list containing numeric values.
            
        Returns:
            list: The same list sorted in descending order.
        """
        return sorted(data_list, reverse=True)

if __name__ == '__main__':
    # Hard-coded sample values for testing the Sorter class functionality
    sorter = Sorter()
    
    # Sample input data containing mixed numbers (integers and floats)
    sample_numbers = [3.5, 10, -2, 7, 4.9, 8]
    
    print("Original list:", sample_numbers)
    sorted_list = sorter.sort_list(sample_numbers)
    print("Sorted list (descending):", sorted_list)