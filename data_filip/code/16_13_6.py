import itertools

def run_length_encode(data):
    if not data:
        return []
    result = []
    for value, group in itertools.groupby(data):
        count = sum(1 for _ in group)
        result.append((value, count))
    return result

if __name__ == '__main__':
    sample_data = [1, 1, 1, 2, 2, 3, 3, 3, 3]
    encoded = run_length_encode(sample_data)
    print(encoded)