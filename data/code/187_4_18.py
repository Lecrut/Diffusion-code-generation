def find_largest(data):
    if not data:
        return None
    try:
        max_value = max(data)
        return max_value
    except TypeError:
        raise ValueError("List must contain only numeric elements")

if __name__ == '__main__':
    list1 = [3, 1, 4, 1, 5, 9, 2]
    print(find_largest(list1))
    list2 = [-10, -5, -20, -1]
    print(find_largest(list2))
    list3 = ['a', 'b', 'c']
    try:
        print(find_largest(list3))
    except ValueError as e:
        print(e)