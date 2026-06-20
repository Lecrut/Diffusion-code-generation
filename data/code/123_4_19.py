def calculate_tuple_sum(data):
    total = 0
    for item in data:
        if not isinstance(item, (int, float)):
            raise TypeError("Tuple must contain only integers or floats.")
        total += item
    return total

if __name__ == '__main__':
    tuple1 = (1, 2.5, 3)
    tuple2 = (4.5, 6, 7)
    tuple3 = (1, 2, 'a', 4)
    tuple4 = ()

    try:
        sum1 = calculate_tuple_sum(tuple1)
        print(f"Sum of {tuple1}: {sum1}")
        sum2 = calculate_tuple_sum(tuple2)
        print(f"Sum of {tuple2}: {sum2}")
        print("Testing error handling:")
        sum3 = calculate_tuple_sum(tuple3)
    except TypeError as e:
        print(e)

    try:
        sum4 = calculate_tuple_sum(tuple4)
    except TypeError as e:
        print(e)