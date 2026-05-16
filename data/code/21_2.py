class Sorter:
    def sort_list(self, data_list):
        data_list.sort(reverse=True)
        return data_list
if __name__ == '__main__':
    sorter = Sorter()
    sample_data = [5, 2, 8, 1, 9, 4]
    sorted_data = sorter.sort_list(sample_data)
    print(sorted_data)