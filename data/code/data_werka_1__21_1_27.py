class Sorter:
    def sort_list(self, data_list):
        return sorted(data_list, reverse=True)

if __name__ == '__main__':
    sample_data = [5, 3, 9, 1, 4]
    sorter_instance = Sorter()
    sorted_data = sorter_instance.sort_list(sample_data)
    print(sorted_data)