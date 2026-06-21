import itertools

def run_length_encode(iterable):
    result = []
    for key, group in itertools.groupby(iterable):
        count = sum(1 for _ in group)
        result.append((key, count))
    return result

if __name__ == '__main__':
    data = 'AAABBBCCCC'
    encoded = run_length_encode(data)
    print(encoded)