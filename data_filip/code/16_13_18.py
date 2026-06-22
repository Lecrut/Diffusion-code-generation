import itertools

def run_length_encode(data):
    if not data:
        return []
    return [(value, len(list(group))) for value, group in itertools.groupby(data)]

if __name__ == '__main__':
    sample_data = [1, 1, 2, 3, 3, 3, 4, 4, 4, 4]
    result = run_length_encode(sample_data)
    print(result)