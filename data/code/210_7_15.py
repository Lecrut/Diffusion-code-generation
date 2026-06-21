def calculate_range(data):
    if not data:
        raise ValueError("Input list is empty")
    for item in data:
        if not isinstance(item, (int, float)):
            raise ValueError("List contains non-numeric types")
    minimum = min(data)
    maximum = max(data)
    return maximum - minimum

if __name__ == '__main__':
    sample_data1 = [10, 5.5, 20, 3.14]
    try:
        result1 = calculate_range(sample_data1)
        print(f"Range of {sample_data1}: {result1}")
    except ValueError as e:
        print(e)

    sample_data2 = [-5, 100, 0.5, -10]
    try:
        result2 = calculate_range(sample_data2)
        print(f"Range of {sample_data2}: {result2}")
    except ValueError as e:
        print(e)

    sample_data3 = [7]
    try:
        result3 = calculate_range(sample_data3)
        print(f"Range of {sample_data3}: {result3}")
    except ValueError as e:
        print(e)

    sample_data4 = []
    try:
        result4 = calculate_range(sample_data4)
        print(f"Range of {sample_data4}: {result4}")
    except ValueError as e:
        print(e)