import itertools

def run_length_encode(data):
    if not data:
        return []
    
    result = []
    for char, group in itertools.groupby(data):
        count = sum(1 for _ in group)
        result.append((char, count))
    return result

if __name__ == '__main__':
    sample_string = "aaabbcccc"
    encoded = run_length_encode(sample_string)
    print(encoded)