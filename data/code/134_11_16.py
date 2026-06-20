def has_overlapping_elements(tup1, tup2, tup3):
    return not set(tup1) & set(tup2) | set(tup2) & set(tup3) | set(tup1) & set(tup3)
if __name__ == '__main__':
    sample_tup1 = (1, 2, 3)
    sample_tup2 = (4, 5, 6)
    sample_tup3 = (7, 8, 9)
    print(has_overlapping_elements(sample_tup1, sample_tup2, sample_tup3))
    sample_tup1 = (1, 2, 3)
    sample_tup2 = (3, 4, 5)
    sample_tup3 = (6, 7, 8)
    print(has_overlapping_elements(sample_tup1, sample_tup2, sample_tup3))