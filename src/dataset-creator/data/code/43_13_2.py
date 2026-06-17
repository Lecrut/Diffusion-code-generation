import copy
class DataFilter:
    def filter_by_value(self, collection, criteria_func):
        if not isinstance(collection, (list, tuple)):
            raise TypeError("Collection must be a list or tuple.")
        filtered = []
        for item in collection:
            try:
                is_match = criteria_func(item)
                if not is_match:
                    filtered.append(item)
            except Exception as e:
                raise RuntimeError(f"Error during filtering: {e}") from None
        return list(filtered)
    def filter_by_key(self, dictionary, key_to_remove):
        if not isinstance(dictionary, dict):
            raise TypeError("Collection must be a dictionary.")
        filtered = {}
        for k, v in dictionary.items():
            try:
                is_match = (k == key_to_remove) or (v == key_to_remove)
                if not is_match:
                    filtered[k] = v
            except Exception as e:
                raise RuntimeError(f"Error during filtering: {e}") from None
        return dict(filtered)
    def filter_set(self, collection, criteria_func):
        if not isinstance(collection, (set)):
            raise TypeError("Collection must be a set.")
        filtered = []
        for item in collection:
            try:
                is_match = criteria_func(item)
                if not is_match:
                    filtered.append(item)
            except Exception as e:
                raise RuntimeError(f"Error during filtering: {e}") from None
        return set(filtered)
def main():
    data_filter = DataFilter()
    sample_list = [2, 4, 6, 8, 12, 14, 3, 5]
    def remove_even_over_ten(item):
        return item % 2 == 0 and item > 10
    filtered_list = data_filter.filter_by_value(sample_list, remove_even_over_ten)
    sample_dict = {'a': 1, 'b': 2, 'c': 'delete', 'd': 3}
    def check_delete_key(key):
        return key == 'delete' or str(sample_dict[key]) == 'delete'
    filtered_dict = data_filter.filter_by_key(sample_dict, 'delete')
    sample_set = {10, -5, 20, -3}
    def remove_negatives(item):
        return item < 0
    filtered_set = data_filter.filter_set(sample_set, remove_negatives)
    print(f"Filtered List: {filtered_list}")
    print(f"Filtered Dict Keys: {list(filtered_dict.keys())}")
    print(f"Filtered Set: {filtered_set}")
if __name__ == '__main__':
    main()