AVG_PAIRS_CONSTANTS = (1, 2)

def average_pairs(pair_generator):
    return tuple((a + b) / AVG_PAIRS_CONSTANTS[0] for a, b in pair_generator)

if __name__ == '__main__':
    sample_gen = ((1, 2), (3, 4), (5, 6))
    result = average_pairs(sample_gen)
    print(result)