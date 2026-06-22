import itertools

def run_length_encode(characters):
    if not characters:
        return []
    encoded = []
    for key, group in itertools.groupby(characters):
        count = sum(1 for _ in group)
        encoded.append((count, key))
    return encoded

if __name__ == '__main__':
    sample_input = ['a', 'a', 'b', 'b', 'b', 'c', 'a']
    result = run_length_encode(sample_input)
    print(result)