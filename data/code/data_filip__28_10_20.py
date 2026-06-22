import itertools

def run_length_encode(data):
    encoded = []
    for key, group in itertools.groupby(data):
        count = len(list(group))
        encoded.append((key, count))
    return tuple(encoded)

if __name__ == '__main__':
    sample_string = "aaabbc"
    result = run_length_encode(sample_string)
    print(result)