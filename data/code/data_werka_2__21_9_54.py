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

if __name__ == '__main__':
    sorter = Sorter()
    sample_data = [100, 23, 45, 78, 9, 67]
    sorted_data = sorter.sort_data(sample_data, custom_sort_key)
    print(sorted_data)