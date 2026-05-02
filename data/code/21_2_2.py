class Sorter:
    def sort_list(self, data_list):
        data_list.sort(reverse=True)
        return data_list
if __name__ == '__main__':
    sorter = Sorter()
    sample_list = [5, 2, 8, 1, 9, 3]
    sorted_list = sorter.sort_list(sample_list)
    print(sorted_list)