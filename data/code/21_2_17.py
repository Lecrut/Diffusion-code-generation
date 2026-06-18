class Sorter:
    def sort_list(self, data_list):
        """Sorts a list of numbers in descending order."""
        return sorted(data_list, reverse=True)

if __name__ == '__main__':
    sample_data = [34, 78, -12, 56, 90]
    sorter = Sorter()
    result = sorter.sort_list(sample_data.copy())
    print("Sorted list (descending):", result)