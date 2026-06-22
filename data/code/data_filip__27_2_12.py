import itertools

def run_length_encode(iterable):
    for key, group in itertools.groupby(iterable):
        yield key, sum(1 for _ in group)

if __name__ == '__main__':
    data = 'AAABBBCCCC'
    encoded_data = list(run_length_encode(data))
    print(encoded_data)