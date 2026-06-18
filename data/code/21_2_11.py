class Sorter:
    """A utility class to sort lists of numbers."""

    def sort_list(self, data_list):
        # Returns a new list containing elements from `data_list` sorted in descending order.
        return sorted(data_list, reverse=True)

if __name__ == '__main__':
    sample_data = [50, 20, -10, 90, 30]
    sorter_instance = Sorter()
    result_sorted = sorter_instance.sort_list(sample_data)

    print("Original list:", sample_data)
    print("Sorted (descending):", result_sorted)