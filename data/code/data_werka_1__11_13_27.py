def compute_length_ratio(tuple1, tuple2):
    len1 = len(tuple1)
    len2 = len(tuple2)
    if len2 == 0:
        return float('inf')
    return len1 / len2
if __name__ == '__main__':
    sample_tuple1 = (1, 2, 3)
    sample_tuple2 = (4, 5)
    ratio = compute_length_ratio(sample_tuple1, sample_tuple2)
    print(ratio)