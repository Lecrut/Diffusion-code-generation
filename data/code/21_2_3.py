class Sorter:
    def sort_list(self, data_list):
        """Sorts the provided list of numbers in reverse (descending) order."""
        sorted_data = sorted(data_list, reverse=True)
        return sorted_data

if __name__ == '__main__':
    sample_numbers = [5, 2, 8, 1, 9]
    sorter = Sorter()
    result = sorter.sort_list(sample_numbers)
    print("Sorted list:", result)