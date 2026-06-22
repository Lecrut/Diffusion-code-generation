import itertools

def run_length_encode(data):
    if not data:
        return []
    return [(len(list(group)), value) for value, group in itertools.groupby(data)]

if __name__ == '__main__':
    sample = [1, 1, 2, 3, 3, 3, 4, 4]
    result = run_length_encode(sample)
    print(result)