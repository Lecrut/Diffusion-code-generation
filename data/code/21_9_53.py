from functools import cmp_to_key

class Sorter:
    def sort_data(self, data_list, key_function):
        if callable(key_function) and not isinstance(key_function, cmp_to_key):
            return sorted(data_list, key=key_function)
        elif isinstance(key_function, cmp_to_key):
            return sorted(data_list, key=key_function)
        else:
            raise ValueError("Unsupported key function type")

def custom_sort_key(x):
    return len(str(x))

def reverse_custom_sort_key(x, y):
    if x < y:
        return 1
    elif x > y:
        return -1
    else:
        return 0

if __name__ == '__main__':
    sorter = Sorter()
    sample_data_1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_data_1 = sorter.sort_data(sample_data_1, custom_sort_key)
    print("Sorted by length of string representation:", sorted_data_1)

    sample_data_2 = [5, 2, 9, 1, 5, 6]
    sorted_data_2 = sorter.sort_data(sample_data_2, cmp_to_key(reverse_custom_sort_key))
    print("Sorted in reverse order using custom comparator:", sorted_data_2)