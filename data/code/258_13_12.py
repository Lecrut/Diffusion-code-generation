def average_pairs(t1, t2):
    return tuple((x + y) / 2 for x, y in zip(t1, t2))

if __name__ == '__main__':
    tuple_a = (7, 8, 9)
    tuple_b = (3, 6, 4)
    averages = average_pairs(tuple_a, tuple_b)
    print(averages)