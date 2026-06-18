class Sorter:
    """A utility class to sort lists of numbers."""
    
    def sort_list(self, data_list):
        """Sorts a list of numbers in descending (reverse) order.
        
        Args:
            data_list: A list containing numerical values.
            
        Returns:
            The sorted list in reverse order.
        """
        return sorted(data_list, reverse=True)

if __name__ == '__main__':
    # Hard-coded sample values for testing without external input or files
    sample_data = [50, 12, 89, 3, -4, 67]
    
    sorter_instance = Sorter()
    sorted_result = sorter_instance.sort_list(sample_data)
    
    print("Sorted list in descending order:")
    for num in sorted_result:
        print(num)