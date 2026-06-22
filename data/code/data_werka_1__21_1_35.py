class Sorter:
    def sort_list(self, data_list):
        return sorted(data_list, reverse=True)

if __name__ == '__main__':
    sample_data = [5, 3, 8, 1, 2, 7]
    sorter_instance = Sorter()
    sorted_data = sorter_instance.sort_list(sample_data)
    print(sorted_data)