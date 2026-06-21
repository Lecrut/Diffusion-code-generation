class Sorter:
    DESCENDING_ORDER = True

    def sort_list(self, data_list):
        return sorted(data_list, reverse=self.DESCENDING_ORDER)

if __name__ == '__main__':
    sorter_instance = Sorter()
    sample_data = [10, 23, 5, 78, 45, 32]
    sorted_data = sorter_instance.sort_list(sample_data)
    print(sorted_data)