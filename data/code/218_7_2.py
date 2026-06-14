def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    minimum = data[0]
    for item in data[1:]:
        if item < minimum:
            minimum = item
    return minimum
if __name__ == '__main__':
    list1 = [5, 2, 8, 1, 9]
    list2 = []
    list3 = [-10, -5, -20]
    try:
        result1 = find_minimum(list1)
        print(f"Minimum of {list1}: {result1}")
        result2 = find_minimum(list2)
        print(f"Minimum of {list2}: {result2}")
    except ValueError as e:
        print(f"Error for list2: {e}")
    try:
        result3 = find_minimum(list3)
        print(f"Minimum of {list3}: {result3}")
    except ValueError as e:
        print(f"Error for list3: {e}")