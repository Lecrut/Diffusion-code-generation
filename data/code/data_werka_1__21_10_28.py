from functools import cmp_to_key

class Sorter:
    def sort_data(self, data_list, key_function):
        return sorted(data_list, key=key_function)

def custom_sort_key(x, y):
    if x['age'] < y['age']:
        return -1
    elif x['age'] > y['age']:
        return 1
    else:
        return 0

if __name__ == '__main__':
    sorter = Sorter()
    sample_data = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25},
        {'name': 'Charlie', 'age': 35}
    ]
    sorted_data = sorter.sort_data(sample_data, cmp_to_key(custom_sort_key))
    print(sorted_data)