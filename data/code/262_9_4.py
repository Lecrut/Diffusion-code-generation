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
    list1 = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"List: {list1}")
    min1, max1 = find_min_max_recursive(list1)
    print(f"Smallest element: {min1}")
    print(f"Largest element: {max1}")
    list2 = [-10, 5, -3, 8, 0]
    print(f"\nList: {list2}")
    min2, max2 = find_min_max_recursive(list2)
    print(f"Smallest element: {min2}")
    print(f"Largest element: {max2}")
    list3 = [42]
    print(f"\nList: {list3}")
    min3, max3 = find_min_max_recursive(list3)
    print(f"Smallest element: {min3}")
    print(f"Largest element: {max3}")
    list4 = []
    print(f"\nList: {list4}")
    min4, max4 = find_min_max_recursive(list4)
    print(f"Smallest element: {min4}")
    print(f"Largest element: {max4}")