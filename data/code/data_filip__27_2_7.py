from itertools import groupby

def run_length_encode(iterable):
    for key, group in groupby(iterable):
        yield (key, sum(1 for _ in group))

if __name__ == '__main__':
    sample = 'AAABBBCCCC'
    result = list(run_length_encode(sample))
    print(result)