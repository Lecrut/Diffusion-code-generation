from itertools import groupby

def run_length_encode(characters):
    result = []
    for char, group in groupby(characters):
        count = len(list(group))
        result.append((count, char))
    return result

if __name__ == '__main__':
    sample_input = ['a', 'a', 'b', 'b', 'b', 'c', 'd', 'd', 'd', 'd']
    encoded = run_length_encode(sample_input)
    print(encoded)