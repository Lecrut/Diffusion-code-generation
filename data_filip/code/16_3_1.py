from itertools import groupby

def run_length_encode(data):
    if not data:
        return []
    result = []
    for key, group in groupby(data):
        count = sum(1 for _ in group)
        result.append((count, key))
    return result

if __name__ == '__main__':
    sample_data = ['a', 'a', 'a', 'b', 'b', 'c', 'a', 'a', 'a', 'a']
    encoded = run_length_encode(sample_data)
    print(encoded)