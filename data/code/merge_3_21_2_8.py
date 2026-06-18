class Sorter:
    def sort_list(self, data_list):
        """Sorts a list of numbers in descending (reverse) order."""
        return sorted(data_list, reverse=True)

if __name__ == '__main__':
    sample_data = [5, 2, 9, 1, 7, 3]
    sorter_instance = Sorter()
    sorted_result = sorter_instance.sort_list(sample_data)

    # Print the original list
    print("Original List:", sample_data)

    # Print the reverse-sorted list
    print("Sorted List (Descending):", sorted_result)