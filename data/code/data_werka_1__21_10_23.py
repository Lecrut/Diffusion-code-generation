from functools import cmp_to_key

class Sorter:

    def sort_data(self, data_list, key_function):
        return sorted(data_list, key=key_function)

def custom_sort_key(item):
    return len(str(item))
if __name__ == '__main__':
    sorter = Sorter()
    sample_data = [5, 'apple', 3.14, 'banana', (1, 2), {'key': 'value'}]
    sorted_data = sorter.sort_data(sample_data, custom_sort_key)
    print(sorted_data)