import itertools

def run_length_encode(data):
    if not data:
        return []
    encoded = []
    for char, group in itertools.groupby(data):
        count = sum(1 for _ in group)
        encoded.append((char, count))
    return encoded

if __name__ == '__main__':
    sample_string = "AAABBBCCDA"
    result = run_length_encode(sample_string)
    print(result)