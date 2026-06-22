def compare_min_max(tuple1, tuple2):
    if not (isinstance(tuple1, tuple) and isinstance(tuple2, tuple)):
        raise ValueError("Both inputs must be tuples")
    
    min_val = min(min(tuple1), min(tuple2))
    max_val = max(max(tuple1), max(tuple2))
    
    return min_val, max_val

if __name__ == '__main__':
    sample_tuple1 = (3, 7, 5)
    sample_tuple2 = (8, 2, 9)
    result = compare_min_max(sample_tuple1, sample_tuple2)
    print(f"Minimum: {result[0]}")
    print(f"Maximum: {result[1]}")