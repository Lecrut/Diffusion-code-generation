def find_largest(data):
    if not data:
        raise ValueError("Cannot find the largest element in an empty list.")
    largest = data[0]
    for item in data[1:]:
        if item > largest:
            largest = item
    return largest

if __name__ == '__main__':
    sample_data1 = [12, 45, 3, 78, 9]
    sample_data2 = [-1, -4, -67, -89, -32]
    try:
        result1 = find_largest(sample_data1)
        print(f"The largest element in {sample_data1} is: {result1}")
    except ValueError as e:
        print(e)
    try:
        result2 = find_largest(sample_data2)
        print(f"The largest element in {sample_data2} is: {result2}")
    except ValueError as e:
        print(e)