def get_middle_value(data):
    if not data:
        return None
    index = len(data) // 2
    return data[index]

if __name__ == '__main__':
    test_lists = [
        [1, 2, 3],
        [10, 20, 30, 40],
        ['a', 'b', 'c', 'd', 'e'],
        [7],
        [5, 9]
    ]
    for items in test_lists:
        print(items, get_middle_value(items))