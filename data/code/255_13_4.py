def find_maximum(data):
    if not data:
        raise ValueError("Input iterable cannot be empty")
    maximum = data[0]
    for item in data[1:]:
        if item > maximum:
            maximum = item
    return maximum
if __name__ == '__main__':
    list1 = [3.14, 1.618, 2.718, 0.577]
    list2 = [-10.5, -5.2, -20.1, -1.3]
    empty_list = []
    try:
        max1 = find_maximum(list1)
        print(f"Maximum of {list1}: {max1}")
        max2 = find_maximum(list2)
        print(f"Maximum of {list2}: {max2}")
        find_maximum(empty_list)
    except ValueError as e:
        print(f"Error caught: {e}")