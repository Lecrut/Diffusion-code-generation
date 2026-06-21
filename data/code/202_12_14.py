def validate_input(data_list):
    if not data_list:
        raise ValueError("Input list cannot be empty")

def convert_to_floats(data_list):
    return [float(item) for item in data_list]

def find_maximum(numbers):
    maximum = numbers[0]
    for number in numbers[1:]:
        if number > maximum:
            maximum = number
    return maximum

if __name__ == '__main__':
    sample_data1 = [10, 5, 20, 8, 15]
    sample_data2 = [-5, -1, -10, -3]
    sample_data3 = [42]
    sample_data4 = []

    try:
        validate_input(sample_data1)
        float_data1 = convert_to_floats(sample_data1)
        result1 = find_maximum(float_data1)
        print(f"Maximum of {sample_data1}: {result1}")

        validate_input(sample_data2)
        float_data2 = convert_to_floats(sample_data2)
        result2 = find_maximum(float_data2)
        print(f"Maximum of {sample_data2}: {result2}")

        validate_input(sample_data3)
        float_data3 = convert_to_floats(sample_data3)
        result3 = find_maximum(float_data3)
        print(f"Maximum of {sample_data3}: {result3}")

    except ValueError as e:
        print(e)