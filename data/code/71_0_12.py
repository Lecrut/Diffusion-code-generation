def find_middle_element(data):
    n = len(data)
    middle_index = n // 2
    return data[middle_index]

if __name__ == '__main__':
    lists = {
        'list1': [1, 2, 3, 4, 5],
        'list2': [10, 20, 30],
        'list3': [7],
        'list4': [100, 200, 300, 400, 500, 600]
    }
    
    for key, value in lists.items():
        print(f"{key}: {find_middle_element(value)}")