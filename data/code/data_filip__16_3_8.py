import itertools

def run_length_encode(chars):
    if not chars:
        return []
    result = []
    for key, group in itertools.groupby(chars):
        count = sum(1 for _ in group)
        result.append((key, count))
    return result

if __name__ == '__main__':
    sample_input = ['a', 'a', 'a', 'b', 'b', 'c', 'a', 'a']
    encoded_result = run_length_encode(sample_input)
    print(encoded_result)