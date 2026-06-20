def sum_mixed_tuple(data):
    total = 0
    for item in data:
        if not isinstance(item, (int, float)):
            raise TypeError("Tuple must contain only integers or floats.")
        total += item
    return total

if __name__ == '__main__':
    sample1 = (1, 2.5, 3)
    sample2 = (4.5, 6, 'a')
    sample3 = ()
    
    try:
        result1 = sum_mixed_tuple(sample1)
        print(f"Sum of {sample1}: {result1}")
        result2 = sum_mixed_tuple(sample2)
        print(f"Attempting to calculate sum for {sample2}...")
    except TypeError as e:
        print(e)