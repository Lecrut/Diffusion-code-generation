def flatten_tuple(tup):
    return [x for x in tup for _ in range(5)]

if __name__ == '__main__':
    sample = (1, 2, 3)
    print(flatten_tuple(sample))