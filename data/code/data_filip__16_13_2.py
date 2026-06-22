import itertools

def run_length_encode(data):
    return [(k, sum(1 for _ in g)) for k, g in itertools.groupby(data)]

if __name__ == '__main__':
    sample = [1, 1, 2, 2, 2, 3, 4, 4, 4, 4]
    print(run_length_encode(sample))