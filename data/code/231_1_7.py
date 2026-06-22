import itertools

def extend_sequence(base_sequence, target_length):
    return list(itertools.islice(itertools.cycle(base_sequence), target_length))

if __name__ == '__main__':
    base_sequence = [1, 2, 3]
    target_length = 15
    result = extend_sequence(base_sequence, target_length)
    print(result)