from functools import cmp_to_key

class Sorter:
    def sort_data(self, data_list, key_function):
        self._validate_input(data_list, key_function)
        if callable(key_function) and not isinstance(key_function, cmp_to_key):
            return sorted(data_list, key=key_function)
        elif isinstance(key_function, cmp_to_key):
            return sorted(data_list, key=key_function)
        else:
            raise ValueError("Unsupported key function type")
    
    def _validate_input(self, data_list, key_function):
        if not isinstance(data_list, list):
            raise ValueError("Data list must be a list")
        if not callable(key_function) and not isinstance(key_function, cmp_to_key):
            raise ValueError("Key function must be callable or an instance of cmp_to_key")

def custom_sort_key(x, y):
    if x < y:
        return -1
    elif x > y:
        return 1
    else:
        return 0

if __name__ == '__main__':
    sorter = Sorter()
    sample_data = [5, 3, 8, 6, 2, 7]
    sorted_data = sorter.sort_data(sample_data, cmp_to_key(custom_sort_key))
    print(sorted_data)