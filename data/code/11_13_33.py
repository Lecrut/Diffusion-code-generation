def compute_length_ratio(tuple1, tuple2):
    return len(tuple1) / len(tuple2)

if __name__ == '__main__':
    sample_tuple1 = (1, 2, 3, 4, 5)
    sample_tuple2 = (6, 7, 8)
    ratio = compute_length_ratio(sample_tuple1, sample_tuple2)
    print(ratio)