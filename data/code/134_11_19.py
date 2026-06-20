def has_overlapping_elements(tuple1, tuple2, tuple3):
    set1 = set(tuple1)
    set2 = set(tuple2)
    set3 = set(tuple3)
    return not (set1.isdisjoint(set2) and set1.isdisjoint(set3) and set2.isdisjoint(set3))

if __name__ == '__main__':
    sample_tuple1 = (1, 2, 3)
    sample_tuple2 = (4, 5, 6)
    sample_tuple3 = (7, 8, 9)
    print(has_overlapping_elements(sample_tuple1, sample_tuple2, sample_tuple3))