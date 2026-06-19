from functools import cmp_to_key

class Sorter:

    def sort_data(self, data_list, key_function):
        return sorted(data_list, key=key_function)

def sample_key_function(x):
    return x[1]
if __name__ == '__main__':
    sorter = Sorter()
    data = [(1, 'apple'), (2, 'orange'), (3, 'banana')]
    sorted_data = sorter.sort_data(data, sample_key_function)
    print(sorted_data)