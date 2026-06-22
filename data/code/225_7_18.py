def compare_min_max(tuple1, tuple2):
    if not all(isinstance(tup, tuple) and len(tup) > 0 for tup in [tuple1, tuple2]):
        raise ValueError("Both inputs must be non-empty tuples.")
    
    min_val = min(min(tuple1), min(tuple2))
    max_val = max(max(tuple1), max(tuple2))
    
    return min_val, max_val

if __name__ == '__main__':
    sample_tuple1 = (3, 5, 7)
    sample_tuple2 = (8, 2, 9)
    result = compare_min_max(sample_tuple1, sample_tuple2)
    print(f"Minimum: {result[0]}")
    print(f"Maximum: {result[1]}")