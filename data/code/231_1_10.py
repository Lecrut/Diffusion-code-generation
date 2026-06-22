import itertools

def create_repeating_sequence(length):
    sequence = [1, 2, 3]
    cycle_iter = itertools.cycle(sequence)
    result = []
    for _ in range(length):
        result.append(next(cycle_iter))
    return result

if __name__ == '__main__':
    sample_length = 15
    print(create_repeating_sequence(sample_length))