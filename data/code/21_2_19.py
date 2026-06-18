class Sorter:
    def sort_list(self, data_list):
        """Sorts a list of numbers in reverse (descending) order."""
        return sorted(data_list, reverse=True)

if __name__ == '__main__':
    sample_data = [34.5, 12, -7, 890, 6]
    sorter = Sorter()
    result = sorter.sort_list(sample_data)
    print(result)