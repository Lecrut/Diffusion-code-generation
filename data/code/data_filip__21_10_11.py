import itertools

def run_length_encode(data):
    if not data:
        return []
    encoded = []
    for key, group in itertools.groupby(data):
        count = sum(1 for _ in group)
        encoded.append((key, count))
    return encoded

if __name__ == '__main__':
    sample_input = "aaabbccccd"
    result = run_length_encode(sample_input)
    print(result)