class Sorter:
    def sort_list(self, data_list):
        return sorted(data_list, reverse=True)

if __name__ == '__main__':
    sorter = Sorter()
    sample_data = [5, 3, 9, 1, 4]
    sorted_data = sorter.sort_list(sample_data)
    print(sorted_data)