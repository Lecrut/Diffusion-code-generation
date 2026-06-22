def average_pairs(tuple1, tuple2):
    return tuple((a + b) / 2 for a, b in zip(tuple1, tuple2))

if __name__ == '__main__':
    result = average_pairs((10, 20, 30), (40, 50, 60))
    print(result)