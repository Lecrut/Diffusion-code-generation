import itertools

def run_length_encode(characters):
    if not characters:
        return []
    result = []
    for key, group in itertools.groupby(characters):
        count = sum(1 for _ in group)
        result.append((key, count))
    return result

if __name__ == '__main__':
    sample1 = ['a', 'a', 'b', 'b', 'b', 'c']
    sample2 = ['x']
    sample3 = []
    sample4 = ['a', 'b', 'c', 'd']
    sample5 = ['a', 'a', 'a', 'a', 'a']

    print(run_length_encode(sample1))
    print(run_length_encode(sample2))
    print(run_length_encode(sample3))
    print(run_length_encode(sample4))
    print(run_length_encode(sample5))