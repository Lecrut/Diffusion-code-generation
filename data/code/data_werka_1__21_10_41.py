from functools import cmp_to_key

class Sorter:

    def sort_data(self, data_list, key_function):
        return sorted(data_list, key=key_function)

def custom_sort_key(item):
    return (item['age'], item['name'])
if __name__ == '__main__':
    sorter = Sorter()
    sample_data = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 30}]
    sorted_data = sorter.sort_data(sample_data, key_function=custom_sort_key)
    print(sorted_data)