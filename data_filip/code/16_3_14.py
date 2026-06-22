from itertools import groupby

def run_length_encode(chars):
    if not chars:
        return []
    result = []
    for char, group in groupby(chars):
        count = len(list(group))
        result.append((char, count))
    return result

if __name__ == '__main__':
    sample_input = ['a', 'a', 'b', 'c', 'c', 'c', 'd', 'e', 'e']
    encoded_result = run_length_encode(sample_input)
    print(encoded_result)