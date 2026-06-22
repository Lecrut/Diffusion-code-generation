from itertools import groupby

def run_length_encode(chars):
    encoded = []
    for char, group in groupby(chars):
        count = sum(1 for _ in group)
        encoded.append((char, count))
    return encoded

if __name__ == '__main__':
    sample_input = ['a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'c', 'd']
    result = run_length_encode(sample_input)
    print(result)