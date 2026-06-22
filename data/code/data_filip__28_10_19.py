import itertools

def run_length_encode(data):
    if not data:
        return ()
    result = []
    for key, group in itertools.groupby(data):
        count = sum(1 for _ in group)
        result.append((key, count))
    return tuple(result)

if __name__ == '__main__':
    sample = 'AAABBBCCCDAA'
    encoded = run_length_encode(sample)
    print(encoded)