import itertools

def run_length_encode(data):
    return [(len(list(group)), key) for key, group in itertools.groupby(data)]

if __name__ == '__main__':
    sample_data = [1, 1, 1, 2, 2, 3, 3, 3, 3]
    result = run_length_encode(sample_data)
    print(result)