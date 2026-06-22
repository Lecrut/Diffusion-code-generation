def max_adjacent_pairs(tup):
    return tuple(max(a, b) for a, b in zip(tup, tup[1:]))

if __name__ == '__main__':
    sample_tuple = (3, 5, 2, 8, 1)
    print(max_adjacent_pairs(sample_tuple))