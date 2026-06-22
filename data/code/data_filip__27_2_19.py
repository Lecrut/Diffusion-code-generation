import itertools

def run_length_encode(iterable):
    if not hasattr(iterable, '__iter__'):
        raise TypeError("Input must be an iterable")
    for key, group in itertools.groupby(iterable):
        count = 0
        for _ in group:
            count += 1
        yield (key, count)

if __name__ == '__main__':
    sample_data = 'AAABBBCCCC'
    encoded_result = list(run_length_encode(sample_data))
    print(encoded_result)