import itertools

def run_length_encode(data):
    if not data:
        return []
    encoded = []
    for char, group in itertools.groupby(data):
        count = len(list(group))
        encoded.append((char, count))
    return encoded

if __name__ == '__main__':
    sample_string = "WWWWWWWWWWWWBWWWWWWWWWWWWBBB"
    result = run_length_encode(sample_string)
    print(result)