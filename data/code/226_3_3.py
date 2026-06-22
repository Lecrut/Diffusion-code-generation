def flatten_tuple(t):
    return [x for x in t for _ in range(5)]

if __name__ == '__main__':
    sample = (1, 2, 3)
    print(flatten_tuple(sample))