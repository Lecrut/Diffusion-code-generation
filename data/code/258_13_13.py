def calculate_average_pairs(tuple1, tuple2):
    return tuple((a + b) / 2 for a, b in zip(tuple1, tuple2))

if __name__ == '__main__':
    sample_tuple1 = (10, 20, 30)
    sample_tuple2 = (5, 15, 25)
    result = calculate_average_pairs(sample_tuple1, sample_tuple2)
    print(result)