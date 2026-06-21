import itertools

def run_length_encode(iterable):
    if not iterable:
        return
    for key, group in itertools.groupby(iterable):
        yield (key, len(list(group)))

if __name__ == '__main__':
    sample_data = 'AAABBBCCCC'
    encoded_result = list(run_length_encode(sample_data))
    print(encoded_result)