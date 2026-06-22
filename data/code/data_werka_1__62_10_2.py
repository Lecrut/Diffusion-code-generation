def get_second_item(lst):
    if len(lst) < 2:
        return None
    return lst[1]

if __name__ == '__main__':
    sample_lists = {
        'list_1': [10, 20, 30, 40, 50],
        'list_2': [5],
        'list_3': ['a', 'b', 'c'],
        'list_4': []
    }
    
    for name, lst in sample_lists.items():
        print(f"The second item in {name} is: {get_second_item(lst)}")