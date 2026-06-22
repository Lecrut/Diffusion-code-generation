import itertools

def run_length_encode(characters):
    if not characters:
        return []
    result = []
    for char, group in itertools.groupby(characters):
        count = sum(1 for _ in group)
        result.append((char, count))
    return result

def run_length_decode(encoded):
    result = []
    for char, count in encoded:
        result.extend([char] * count)
    return result

if __name__ == '__main__':
    sample_input = ['a', 'a', 'b', 'b', 'b', 'c', 'a', 'a', 'a']
    encoded = run_length_encode(sample_input)
    print(encoded)
    decoded = run_length_decode(encoded)
    print(decoded)