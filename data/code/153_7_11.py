class NestedListChecker:
    @staticmethod
    def flatten_list(nested_list):
        flat_list = []
        for item in nested_list:
            if isinstance(item, list):
                flat_list.extend(NestedListChecker.flatten_list(item))
            else:
                flat_list.append(item)
        return flat_list

    def check_item_existence(self, data, value):
        flattened_data = NestedListChecker.flatten_list(data)
        return value in flattened_data

if __name__ == '__main__':
    checker = NestedListChecker()
    sample_list = [
        [1, 2, [3, 4], 5],
        [6, [7, 8]],
        9,
        10
    ]
    value_to_find = 8
    result1 = checker.check_item_existence(sample_list, value_to_find)
    print(f"Checking for '{value_to_find}': {result1}")

    value_to_find = 11
    result2 = checker.check_item_existence(sample_list, value_to_find)
    print(f"Checking for '{value_to_find}': {result2}")