class TupleSorter:
    def sort_tuple(self, data):
        sorted_list = []
        while data:
            min_value = min(data)
            sorted_list.append(min_value)
            data = tuple(x for x in data if x != min_value)
        return sorted_list

if __name__ == '__main__':
    sorter = TupleSorter()
    sample_data = (3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5)
    sorted_result = sorter.sort_tuple(sample_data)
    print(sorted_result)