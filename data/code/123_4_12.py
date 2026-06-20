def calculate_tuple_sum(data):
    total = 0
    for item in data:
        if not isinstance(item, (int, float)):
            raise TypeError("Tuple must contain only integers or floats.")
        total += item
    return total

if __name__ == '__main__':
    sample_tuple1 = (1, 2, 3.5)
    sample_tuple2 = (4, 5.5, 6)
    sample_tuple3 = (7, "eight", 9)

    try:
        sum1 = calculate_tuple_sum(sample_tuple1)
        print(f"Sum of {sample_tuple1}: {sum1}")
        sum2 = calculate_tuple_sum(sample_tuple2)
        print(f"Sum of {sample_tuple2}: {sum2}")
        print("Testing error handling:")
        sum3 = calculate_tuple_sum(sample_tuple3)
    except TypeError as e:
        print(e)