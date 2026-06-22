from functools import cmp_to_key

class Sorter:
    DEFAULT_KEY_FUNCTION = lambda x: x

    @staticmethod
    def custom_sort_key(x, y):
        if x < y:
            return -1
        elif x > y:
            return 1
        else:
            return 0

    def sort_data(self, data_list, key_function=DEFAULT_KEY_FUNCTION):
        if callable(key_function) and not isinstance(key_function, cmp_to_key):
            return sorted(data_list, key=key_function)
        elif isinstance(key_function, cmp_to_key):
            return sorted(data_list, key=key_function)
        else:
            raise ValueError("Unsupported key function type")

if __name__ == '__main__':
    sorter = Sorter()
    sample_data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_data_with_default_key = sorter.sort_data(sample_data)
    print("Sorted data with default key:", sorted_data_with_default_key)

    custom_cmp_key = cmp_to_key(Sorter.custom_sort_key)
    sorted_data_with_custom_cmp_key = sorter.sort_data(sample_data, custom_cmp_key)
    print("Sorted data with custom compare function:", sorted_data_with_custom_cmp_key)