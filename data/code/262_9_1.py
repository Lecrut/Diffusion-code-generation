def find_min_max_recursive(data):
    if not data:
        return None, None
    if len(data) == 1:
        return data[0], data[0]
    first = data[0]
    rest = data[1:]
    min_rest, max_rest = find_min_max_recursive(rest)
    min_val = min(first, min_rest)
    max_val = max(first, max_rest)
    return min_val, max_val
if __name__ == '__main__':
    list1 = [3, 1, 4, 1, 5, 9, 2, 6]
    list2 = [-10, 5, 0, -20, 100]
    list3 = [7]
    list4 = []
    min1, max1 = find_min_max_recursive(list1)
    print(f"List: {list1}")
    print(f"Smallest element: {min1}")
    print(f"Largest element: {max1}\n")
    min2, max2 = find_min_max_recursive(list2)
    print(f"List: {list2}")
    print(f"Smallest element: {min2}")
    print(f"Largest element: {max2}\n")
    min3, max3 = find_min_max_recursive(list3)
    print(f"List: {list3}")
    print(f"Smallest element: {min3}")
    print(f"Largest element: {max3}\n")
    min4, max4 = find_min_max_recursive(list4)
    print(f"List: {list4}")
    print(f"Smallest element: {min4}")
    print(f"Largest element: {max4}\n")