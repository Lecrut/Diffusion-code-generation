def find_min_max(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    minimum = data[0]
    maximum = data[0]
    for x in data:
        if x < minimum:
            minimum = x
        if x > maximum:
            maximum = x
    return (minimum, maximum)
if __name__ == '__main__':
    list1 = [3, 1, 4, 1, 5, 9, 2, 6]
    result1 = find_min_max(list1)
    print(f"List: {list1}, Min: {result1[0]}, Max: {result1[1]}")
    list2 = [-10, 5, 0, -20, 100]
    result2 = find_min_max(list2)
    print(f"List: {list2}, Min: {result2[0]}, Max: {result2[1]}")
    list3 = [7]
    result3 = find_min_max(list3)
    print(f"List: {list3}, Min: {result3[0]}, Max: {result3[1]}")
    list4 = []
    try:
        find_min_max(list4)
    except ValueError as e:
        print(f"Error for empty list: {e}")