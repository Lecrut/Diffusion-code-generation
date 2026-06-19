class Sorter:
    def sort_list(self, data_list):
        return sorted(data_list, reverse=True)

if __name__ == '__main__':
    sample_values = [5, 2, 9, 1, 5, 6]
    sorter_instance = Sorter()
    sorted_values = sorter_instance.sort_list(sample_values)
    print(sorted_values)