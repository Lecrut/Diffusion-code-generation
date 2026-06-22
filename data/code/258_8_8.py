def average_pairs(generator):
    return tuple((a + b) / 2 for a, b in generator)

if __name__ == '__main__':
    sample_generator = ((1, 2), (3, 4), (5, 6))
    result = average_pairs(sample_generator)
    print(result)