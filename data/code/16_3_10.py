from itertools import groupby

def run_length_encode(chars):
    if not chars:
        return []
    result = []
    for char, group in groupby(chars):
        length = sum(1 for _ in group)
        result.append((char, length))
    return result

if __name__ == '__main__':
    sample_chars = ['a', 'a', 'b', 'b', 'b', 'c', 'c', 'a', 'a']
    encoded = run_length_encode(sample_chars)
    print(encoded)