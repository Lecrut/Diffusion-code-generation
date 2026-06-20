def calculate_tuple_sum(data):
    total = 0
    for item in data:
        if not isinstance(item, (int, float)):
            raise TypeError("Tuple must contain only integers or floats.")
        total += item
    return total

if __name__ == '__main__':
    sample_tuple1 = (1, 2.5, 3)
    sample_tuple2 = (10, 20, 30.5)
    sample_tuple3 = (1, 2, 'a', 4)
    sample_tuple4 = ()

    try:
        sum1 = calculate_tuple_sum(sample_tuple1)
        print(f"Sum of {sample_tuple1}: {sum1}")
        
        sum2 = calculate_tuple_sum(sample_tuple2)
        print(f"Sum of {sample_tuple2}: {sum2}")
        
        print("Testing error handling:")
        
    except TypeError as e:
        print(e)

    try:
        calculate_tuple_sum(sample_tuple3)
    except TypeError as e:
        print(e)

    print("Attempting to calculate sum for empty tuple...")
    try:
        sum4 = calculate_tuple_sum(sample_tuple4)
        print(f"Sum of {sample_tuple4}: {sum4}")
    except ValueError:
        print("Empty tuple, no sum to calculate.")