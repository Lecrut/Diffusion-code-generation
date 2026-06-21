from functools import cmp_to_key

class Sorter:
    def sort_data(self, data_list, key_function):
        if callable(key_function) and not isinstance(key_function, cmp_to_key):
            return sorted(data_list, key=key_function)
        elif isinstance(key_function, cmp_to_key):
            return sorted(data_list, key=key_function)
        else:
            raise ValueError("Unsupported key function type")

def custom_sort_key(x, y):
    if x < y:
        return -1
    elif x > y:
        return 1
    else:
        return 0

if __name__ == '__main__':
    sorter = Sorter()
    sample_data = ['apple', 'banana', 'cherry', 'date']
    category_map = {'fruit': ['apple', 'banana', 'cherry'], 'vegetable': ['carrot']}
    
    def custom_sort_key_with_category(item):
        if item in category_map['fruit']:
            return (0, len(item))
        elif item in category_map['vegetable']:
            return (1, len(item))
        else:
            return (2, len(item))
    
    sorted_data = sorter.sort_data(sample_data, cmp_to_key(custom_sort_key_with_category))
    print(sorted_data)