def validate_data(data):
    if not all(isinstance(item, (int, float)) for item in data):
        raise TypeError("Tuple must contain only integers or floats.")

def calculate_tuple_sum(data):
    validate_data(data)
    return sum(data)

if __name__ == '__main__':
    sample1 = (1, 2, 3.5, 4, 5)
    sample2 = (10, 20, 30.5)
    sample3 = (1, 2, 'a', 4)
    sample4 = ()

    try:
        sum1 = calculate_tuple_sum(sample1)
        print(f"Sum of {sample1}: {sum1}")
        sum2 = calculate_tuple_sum(sample2)
        print(f"Sum of {sample2}: {sum2}")
        print("Testing error handling:")
    except TypeError as e:
        print(e)

    try:
        calculate_tuple_sum(sample3)
    except TypeError as e:
        print(e)

    try:
        calculate_tuple_sum(sample4)
    except TypeError as e:
        print(e)