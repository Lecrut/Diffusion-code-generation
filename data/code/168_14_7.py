def segment_tuples_by_sign(tuples_list):
    positive = [t for t in tuples_list if t[0] > 0]
    negative = [t for t in tuples_list if t[0] < 0]
    return positive, negative

if __name__ == '__main__':
    sample_values = [(-1, 2), (3, -4), (5, 6), (-7, 8)]
    result = segment_tuples_by_sign(sample_values)
    print(result)