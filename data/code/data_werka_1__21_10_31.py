from functools import cmp_to_key

class Sorter:
    def sort_data(self, data_list, key_function):
        return sorted(data_list, key=key_function)

def custom_sort_key(x, y):
    if x[0] < y[0]:
        return -1
    elif x[0] > y[0]:
        return 1
    else:
        return 0

if __name__ == '__main__':
    sorter = Sorter()
    sample_data = [(3, 'c'), (1, 'a'), (2, 'b')]
    sorted_data = sorter.sort_data(sample_data, cmp_to_key(custom_sort_key))
    print(sorted_data)