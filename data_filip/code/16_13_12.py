import itertools

def run_length_encode(data):
    if not data:
        return []
    encoded = []
    for key, group in itertools.groupby(data):
        count = sum(1 for _ in group)
        encoded.append([count, key])
    return encoded

if __name__ == '__main__':
    sample_data = [1, 1, 2, 3, 3, 3, 4]
    result = run_length_encode(sample_data)
    print(result)