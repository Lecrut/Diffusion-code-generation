import itertools

def run_length_encode(data):
    if not data:
        return []
    result = []
    for key, group in itertools.groupby(data):
        count = sum(1 for _ in group)
        result.append((key, count))
    return result

if __name__ == '__main__':
    sample = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 5]
    encoded = run_length_encode(sample)
    print(encoded)