def average_pairs(generator):
    return tuple((a + b) / 2 for a, b in zip(generator, generator))

if __name__ == '__main__':
    sample_generator = (x for x in range(10))
    print(average_pairs(sample_generator))