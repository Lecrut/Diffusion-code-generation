class TupleSorter:
    @staticmethod
    def sort_tuple(data):
        sorted_list = []
        while data:
            min_value = min(data)
            sorted_list.append(min_value)
            data = tuple(x for x in data if x != min_value)
        return sorted_list

if __name__ == '__main__':
    sorter = TupleSorter()
    sample_data = (3, 1, 5, 2, 8)
    sorted_result = sorter.sort_tuple(sample_data)
    print(sorted_result)