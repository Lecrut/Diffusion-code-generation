class ListFlattener:
    @staticmethod
    def flatten_list(nested_list):
        result = []
        for item in nested_list:
            if isinstance(item, list):
                result.extend(ListFlattener.flatten_list(item))
            else:
                result.append(item)
        return result

    @staticmethod
    def check_item_in_flattened_list(flattened_list, value):
        return value in flattened_list

if __name__ == '__main__':
    sample_list = [
        {"id": 1, "name": "Alice", "city": "New York"},
        {"id": 2, "name": "Bob", "city": "Los Angeles"},
        {"id": 3, "name": "Charlie", "city": "New York"}
    ]
    flattened_list = ListFlattener.flatten_list(sample_list)
    value_to_find = "New York"
    result1 = ListFlattener.check_item_in_flattened_list(flattened_list, value_to_find)
    print(f"Checking for '{value_to_find}' in flattened list: {result1}")