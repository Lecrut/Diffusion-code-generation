def compare_min_max(tuple1, tuple2):
    if not (isinstance(tuple1, tuple) and isinstance(tuple2, tuple)):
        raise ValueError("Both inputs must be tuples.")
    
    combined = tuple1 + tuple2
    if len(combined) == 0:
        raise ValueError("One or both input tuples are empty.")
    
    return min(combined), max(combined)

if __name__ == '__main__':
    sample_tuple1 = (5, 10, 15)
    sample_tuple2 = (8, 3, 7)
    try:
        result_min, result_max = compare_min_max(sample_tuple1, sample_tuple2)
        print(f"Combined Minimum: {result_min}")
        print(f"Combined Maximum: {result_max}")
    except ValueError as e:
        print(e)