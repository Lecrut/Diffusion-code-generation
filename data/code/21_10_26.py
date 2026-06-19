from functools import cmp_to_key

class Sorter:
    def sort_data(self, data_list, key_function):
        return sorted(data_list, key=key_function)

def custom_cmp(x, y):
    if x[0] < y[0]:
        return -1
    elif x[0] > y[0]:
        return 1
    else:
        if x[1] < y[1]:
            return -1
        elif x[1] > y[1]:
            return 1
        else:
            return 0

if __name__ == '__main__':
    sorter = Sorter()
    data = [(3, 'apple'), (1, 'banana'), (2, 'cherry'), (2, 'date')]
    sorted_data = sorter.sort_data(data, cmp_to_key(custom_cmp))
    print(sorted_data)