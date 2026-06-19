class Sorter:
    def sort_list(self, data_list):
        return sorted(data_list, reverse=True)

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorter_instance = Sorter()
    sorted_result = sorter_instance.sort_list(sample_values)
    print(sorted_result)