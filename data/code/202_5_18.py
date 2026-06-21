class ListFlattener:
    MAX_VALUE = float('-inf')

    @staticmethod
    def flatten_and_find_largest(data):
        flattened_data = []
        ListFlattener._flatten(data, flattened_data)
        if not flattened_data:
            return None
        largest = ListFlattener.MAX_VALUE
        for item in flattened_data:
            if item > largest:
                largest = item
        return largest

    @staticmethod
    def _flatten(data, result):
        for item in data:
            if isinstance(item, list):
                ListFlattener._flatten(item, result)
            else:
                result.append(item)
if __name__ == '__main__':
    nested_list = [10, [20, [30, 40], 50], 60]
    largest_number = ListFlattener.flatten_and_find_largest(nested_list)
    print(largest_number)