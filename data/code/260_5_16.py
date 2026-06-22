def max_values(tuple1, tuple2):
    return tuple((max(a, b) for a, b in zip(tuple1, tuple2)))
if __name__ == '__main__':
    sample_tuple1 = (10, 20, 30)
    sample_tuple2 = (15, 25, 35)
    result = max_values(sample_tuple1, sample_tuple2)
    print(result)