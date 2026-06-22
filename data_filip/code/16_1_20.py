import itertools

def run_length_encode(lst):
    if not lst:
        return []
    result = []
    for key, group in itertools.groupby(lst):
        count = sum(1 for _ in group)
        result.append((key, count))
    return result

if __name__ == '__main__':
    sample_list = [1, 1, 1, 2, 3, 3, 4, 4, 4, 4]
    encoded = run_length_encode(sample_list)
    print(encoded)