from itertools import groupby

def run_length_encode(iterable):
    for key, group in groupby(iterable):
        count = sum(1 for _ in group)
        yield (key, count)

if __name__ == '__main__':
    sample_data = 'AAABBBCCCC'
    result = list(run_length_encode(sample_data))
    print(result)