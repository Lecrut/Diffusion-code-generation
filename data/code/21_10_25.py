from functools import cmp_to_key

class Sorter:

    def sort_data(self, data_list, key_function):
        return sorted(data_list, key=key_function)

def custom_sort_key(x):
    return x[1]
if __name__ == '__main__':
    sorter = Sorter()
    sample_data = [(1, 'apple'), (3, 'banana'), (2, 'cherry')]
    sorted_data = sorter.sort_data(sample_data, key_function=custom_sort_key)
    print(sorted_data)