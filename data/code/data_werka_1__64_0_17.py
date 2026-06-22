def find_last_occurrence_index(data_list, item):
    last_index = -1
    for index in range(len(data_list) - 1, -1, -1):
        if data_list[index] == item:
            last_index = index
            break
    return last_index

if __name__ == '__main__':
    sample_data = {
        'list1': [1, 5, 2, 8, 5, 3],
        'item1': 5,
        'list2': ['x', 'y', 'z', 'x', 'w', 'x'],
        'item2': 'x',
        'list3': [10, 20, 30, 40, 50],
        'item3': 60,
    }

    for key in sample_data:
        if isinstance(key, str) and key.startswith('list'):
            list_name = key
            item_name = f'item{key[-1]}'
            result = find_last_occurrence_index(sample_data[list_name], sample_data[item_name])
            print(f"List: {sample_data[list_name]}, Item: {sample_data[item_name]}, Last Occurrence Index: {result}")