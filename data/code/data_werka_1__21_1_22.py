class Sorter:
    def sort_list(self, data_list):
        return sorted(data_list, reverse=True)

if __name__ == '__main__':
    sorter_instance = Sorter()
    sample_data = [5, 3, 8, 1, 9, 2]
    sorted_data = sorter_instance.sort_list(sample_data)
    print(sorted_data)