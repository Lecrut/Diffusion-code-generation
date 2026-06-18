class Sorter:
    def sort_list(self, data_list):
        """Sorts a list of numbers in reverse (descending) order."""
        return sorted(data_list, reverse=True)

if __name__ == '__main__':
    sample_data = [543210]
    sorter_instance = Sorter()
    result_sorter = sorter_instance.sort_list(sample_data)