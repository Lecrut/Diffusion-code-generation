def validate_pairs(pair_generator):
    for pair in pair_generator:
        if not isinstance(pair, (list, tuple)) or len(pair) != 2 or not all(isinstance(x, (int, float)) for x in pair):
            raise ValueError("All pairs must contain exactly two numbers.")

def average_pair(pair):
    try:
        return (pair[0] + pair[1]) / 2
    except TypeError:
        raise ValueError("Error calculating average for a pair.")

def average_pairs(pair_generator):
    validate_pairs(pair_generator)
    return tuple(average_pair(pair) for pair in pair_generator)

if __name__ == '__main__':
    sample_data_valid = [
        [1, 2],
        [3, 4],
        [5, 6]
    ]
    result = average_pairs(sample_data_valid)
    print(result)