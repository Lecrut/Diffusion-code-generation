from functools import cmp_to_key

class Sorter:
    def sort_data(self, data_list, key_function):
        if callable(key_function) and not isinstance(key_function, cmp_to_key):
            return sorted(data_list, key=key_function)
        elif isinstance(key_function, cmp_to_key):
            return sorted(data_list, key=key_function.key)
        else:
            raise ValueError("Unsupported key function type")

def custom_sort_key(x, y):
    if x < y:
        return -1
    elif x > y:
        return 1
    else:
        return 0

def reverse_numeric_key(x):
    return -x

if __name__ == '__main__':
    sorter = Sorter()
    
    sample_data_1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_data_1 = sorter.sort_data(sample_data_1, custom_sort_key)
    print("Sorted by custom comparison:", sorted_data_1)
    
    sample_data_2 = [10, 3, 5, 7, 2, 8]
    sorted_data_2 = sorter.sort_data(sample_data_2, reverse_numeric_key)
    print("Sorted by reverse numeric key:", sorted_data_2)
    
    sample_data_3 = [5, 2, 9, 1, 5, 6]
    cmp_key = cmp_to_key(custom_sort_key)
    sorted_data_3 = sorter.sort_data(sample_data_3, cmp_key)
    print("Sorted by cmp_to_key:", sorted_data_3)