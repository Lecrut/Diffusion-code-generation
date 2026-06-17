def find_min_max_recursive(data):
    if not data:
        return None, None
    if len(data) == 1:
        return data[0], data[0]
    else:
        first = data[0]
        rest = data[1:]
        min_rest, max_rest = find_min_max_recursive(rest)
        return min(first, min_rest), max(first, max_rest)
if __name__ == '__main__':
    list1 = [3, 1, 4, 1, 5, 9, 2]
    print(f"List: {list1}")
    min_val1, max_val1 = find_min_max_recursive(list1)
    print(f"Smallest element: {min_val1}")
    print(f"Largest element: {max_val1}")
    list2 = [-10, 5, 0, -20, 100]
    print(f"\nList: {list2}")
    min_val2, max_val2 = find_min_max_recursive(list2)
    print(f"Smallest element: {min_val2}")
    print(f"Largest element: {max_val2}")
    list3 = [7]
    print(f"\nList: {list3}")
    min_val3, max_val3 = find_min_max_recursive(list3)
    print(f"Smallest element: {min_val3}")
    print(f"Largest element: {max_val3}")
    list4 = []
    print(f"\nList: {list4}")
    min_val4, max_val4 = find_min_max_recursive(list4)
    print(f"Smallest element: {min_val4}")
    print(f"Largest element: {max_val4}")