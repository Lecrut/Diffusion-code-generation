class Sorter:
    def sort_list(self, data_list):
        return sorted(data_list, reverse=True)

if __name__ == '__main__':
    sample_values = [5, 3, 8, 1, 2]
    sorter_instance = Sorter()
    sorted_result = sorter_instance.sort_list(sample_values)
    print(sorted_result)