from functools import cmp_to_key

class Sorter:
    def sort_data(self, data_list, key_function):
        if callable(key_function) and not isinstance(key_function, cmp_to_key):
            return sorted(data_list, key=key_function)
        elif isinstance(key_function, cmp_to_key):
            return sorted(data_list, key=key_function)
        else:
            raise ValueError("Unsupported key function type")

def custom_sort_key(x, y):
    if x < y:
        return -1
    elif x > y:
        return 1
    else:
        return 0

if __name__ == '__main__':
    sorter = Sorter()
    sample_data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_data_cmp = sorter.sort_data(sample_data, cmp_to_key(custom_sort_key))
    print("Sorted data using cmp_to_key:", sorted_data_cmp)

    def custom_sort_length(x):
        return len(str(x))

    sorted_data_length = sorter.sort_data(sample_data, custom_sort_length)
    print("Sorted data by length of string representation:", sorted_data_length)