def find_last_occurrence_index(data, item):
    last_index = -1
    for i in range(len(data) - 1, -1, -1):
        if data[i] == item:
            last_index = i
            break
    return last_index

if __name__ == '__main__':
    sample_values = {
        'list1': [1, 5, 2, 8, 5, 3],
        'item1': 5,
        'list2': ['x', 'y', 'z', 'x', 'w'],
        'item2': 'x',
        'list3': [100, 200, 300, 400, 500],
        'item3': 600,
    }
    
    for key in ['list1', 'list2']:
        lst = sample_values[key]
        item = sample_values[f'{key[:-1]}{int(key[-1]) + 1}']
        result = find_last_occurrence_index(lst, item)
        print(f"List: {lst}, Item: {item}, Last Occurrence Index: {result}")
    
    list3 = sample_values['list3']
    item3 = sample_values['item3']
    result3 = find_last_occurrence_index(list3, item3)
    print(f"List: {list3}, Item: {item3}, Last Occurrence Index: {result3}")