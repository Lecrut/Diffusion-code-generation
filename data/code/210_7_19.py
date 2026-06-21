def validate_input(data):
    if not data:
        raise ValueError("Input list is empty")
    for item in data:
        if not isinstance(item, (int, float)):
            raise ValueError("Input list contains non-numeric types")

def calculate_range(data):
    validate_input(data)
    minimum = min(data)
    maximum = max(data)
    return maximum - minimum

if __name__ == '__main__':
    sample_data1 = [10, 5.5, 20, 3.14]
    result1 = calculate_range(sample_data1)
    print(f"Range of {sample_data1}: {result1}")

    sample_data2 = [-5, 100, 0.5, -10]
    result2 = calculate_range(sample_data2)
    print(f"Range of {sample_data2}: {result2}")

    sample_data3 = [7]
    result3 = calculate_range(sample_data3)
    print(f"Range of {sample_data3}: {result3}")

    try:
        sample_data4 = []
        result4 = calculate_range(sample_data4)
        print(f"Range of {sample_data4}: {result4}")
    except ValueError as e:
        print(e)

    try:
        sample_data5 = [10, 5.5, "20", 3.14]
        result5 = calculate_range(sample_data5)
        print(f"Range of {sample_data5}: {result5}")
    except ValueError as e:
        print(e)