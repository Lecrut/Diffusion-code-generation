def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return data[0]

if __name__ == '__main__':
    list1 = [5, 2, 8, 1, 9]
    list2 = []
    try:
        result1 = find_minimum(list1)
        print(f"Minimum of {list1}: {result1}")
        result2 = find_minimum(list2)
        print(f"Minimum of {list2}: {result2}")
    except ValueError as e:
        print(e)