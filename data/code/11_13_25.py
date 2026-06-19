def compute_length_ratio(tuple1, tuple2):
    if not isinstance(tuple1, tuple) or not isinstance(tuple2, tuple):
        raise TypeError("Both inputs must be tuples")
    
    length1 = len(tuple1)
    length2 = len(tuple2)
    
    if length2 == 0:
        return float('inf') if length1 > 0 else 0.0
    
    return length1 / length2

if __name__ == '__main__':
    tuple_a = (1, 2, 3)
    tuple_b = (4, 5)
    
    ratio = compute_length_ratio(tuple_a, tuple_b)
    print(ratio)