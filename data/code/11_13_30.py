def compute_length_ratio(tuple1, tuple2):
    return len(tuple1) / len(tuple2)

if __name__ == '__main__':
    sample_tuple1 = (1, 2, 3)
    sample_tuple2 = (4, 5)
    ratio = compute_length_ratio(sample_tuple1, sample_tuple2)
    print(ratio)