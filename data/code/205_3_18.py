class MinSorter:
    @staticmethod
    def sort_min(data):
        sorted_list = []
        while data:
            min_value = min(data)
            sorted_list.append(min_value)
            data.remove(min_value)
        return sorted_list

if __name__ == '__main__':
    sorter = MinSorter()
    sample_data = [5, 3, 8, 1, 2]
    sorted_result = sorter.sort_min(sample_data)
    print(sorted_result)