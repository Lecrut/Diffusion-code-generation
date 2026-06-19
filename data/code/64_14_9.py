class ListUtils:
    @staticmethod
    def find_last_index(data, target):
        if not data:
            return -1
        for index in range(len(data) - 1, -1, -1):
            if data[index] == target:
                return index
        return -1

if __name__ == '__main__':
    sample_data = [5, 3, 8, 3, 9, 3]
    target_value = 3
    last_index = ListUtils.find_last_index(sample_data, target_value)
    print(last_index)

    sample_data_empty = []
    target_value_empty = 7
    last_index_empty = ListUtils.find_last_index(sample_data_empty, target_value_empty)
    print(last_index_empty)

    sample_data_single = [42]
    target_value_single = 42
    last_index_single = ListUtils.find_last_index(sample_data_single, target_value_single)
    print(last_index_single)