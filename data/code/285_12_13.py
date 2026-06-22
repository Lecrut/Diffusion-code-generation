def max_adjacent_pairs(t):
    return tuple(max(a, b) for a, b in zip(t, t[1:]))

if __name__ == '__main__':
    sample_tuple = (3, 5, 2, 8, 6)
    result = max_adjacent_pairs(sample_tuple)
    print(result)