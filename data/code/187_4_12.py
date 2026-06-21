def find_largest(data):
    if not data:
        return None
    max_value = float('-inf')
    for value in data:
        if isinstance(value, (int, float)) and value > max_value:
            max_value = value
    return max_value

if __name__ == '__main__':
    list1 = [3, 1, 4, 1, 5, 9, 2]
    print(find_largest(list1))
    list2 = [-10, -5, -20, -1]
    print(find_largest(list2))
    empty_list = []
    print(find_largest(empty_list))