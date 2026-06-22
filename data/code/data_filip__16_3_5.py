from itertools import groupby

def run_length_encode(chars):
    if not chars:
        return []
    result = []
    for key, group in groupby(chars):
        count = len(list(group))
        result.append((key, count))
    return result

if __name__ == '__main__':
    sample_input = ['a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'c', 'd']
    encoded_output = run_length_encode(sample_input)
    print(encoded_output)