def find_largest(data):
    if not data:
        raise ValueError("Cannot find the largest element in an empty list.")
    largest = data[0]
    for item in data[1:]:
        if item > largest:
            largest = item
    return largest
if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 3]
    list2 = []
    list3 = [-10, -5, -20]
    try:
        result1 = find_largest(list1)
        print(f"Largest in {list1}: {result1}")
    except ValueError as e:
        print(f"Error for {list1}: {e}")
    try:
        result2 = find_largest(list2)
        print(f"Largest in {list2}: {result2}")
    except ValueError as e:
        print(f"Error for {list2}: {e}")
    try:
        result3 = find_largest(list3)
        print(f"Largest in {list3}: {result3}")
    except ValueError as e:
        print(f"Error for {list3}: {e}")