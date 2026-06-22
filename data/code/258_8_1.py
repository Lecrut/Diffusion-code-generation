def average_pairs(gen):
    return tuple((a + b) / 2 for a, b in gen)

if __name__ == '__main__':
    sample_gen = ((1, 2), (3, 4), (5, 6))
    result = average_pairs(sample_gen)
    print(result)