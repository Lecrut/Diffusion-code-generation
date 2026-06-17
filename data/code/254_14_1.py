def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return min(data)
if __name__ == '__main__':
    list1 = [5, 2, 8, 1]
    list2 = []
    try:
        result1 = find_minimum(list1)
        print(f"Minimum of {list1}: {result1}")
    except ValueError as e:
        print(f"Error for list1: {e}")
    try:
        result2 = find_minimum(list2)
        print(f"Minimum of {list2}: {result2}")
    except ValueError as e:
        print(f"Error for list2: {e}")