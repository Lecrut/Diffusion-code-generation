def compute_length_ratio(tuple1: tuple, tuple2: tuple) -> float:
    if not isinstance(tuple1, tuple) or not isinstance(tuple2, tuple):
        raise TypeError("Both arguments must be tuples.")
    
    length1 = len(tuple1)
    length2 = len(tuple2)
    
    if length2 == 0:
        raise ValueError("The second tuple cannot have a length of zero to avoid division by zero.")
    
    return length1 / length2

if __name__ == '__main__':
    sample_tuple1 = (1, 2, 3, 4, 5)
    sample_tuple2 = (6, 7, 8)
    ratio = compute_length_ratio(sample_tuple1, sample_tuple2)
    print(ratio)