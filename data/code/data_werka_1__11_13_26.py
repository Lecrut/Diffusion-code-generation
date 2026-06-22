def compute_length_ratio(tuple1: tuple, tuple2: tuple) -> float:
    if len(tuple2) == 0:
        raise ValueError("The second tuple must not be empty to avoid division by zero.")
    return len(tuple1) / len(tuple2)

if __name__ == '__main__':
    sample_tuple1 = (1, 2, 3, 4)
    sample_tuple2 = (5, 6)
    ratio = compute_length_ratio(sample_tuple1, sample_tuple2)
    print(ratio)