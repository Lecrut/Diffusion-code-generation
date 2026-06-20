def sum_mixed_tuple(data):
    total = 0
    for item in data:
        if not isinstance(item, (int, float)):
            raise TypeError("Tuple must contain only integers or floats.")
        total += item
    return total

if __name__ == '__main__':
    tuple1 = (1, 2.5, 3, 4)
    tuple2 = (10, 20, 30)
    tuple3 = (1, 2, 'a', 4)
    tuple4 = ()
    
    try:
        sum1 = sum_mixed_tuple(tuple1)
        print(f"Sum of {tuple1}: {sum1}")
        sum2 = sum_mixed_tuple(tuple2)
        print(f"Sum of {tuple2}: {sum2}")
        print("Testing error handling:")
        sum3 = sum_mixed_tuple(tuple3)
    except TypeError as e:
        print(e)
    
    try:
        sum4 = sum_mixed_tuple(tuple4)
        print(f"Sum of {tuple4}: {sum4}")
    except TypeError as e:
        print(e)