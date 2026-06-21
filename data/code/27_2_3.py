from itertools import groupby

def run_length_encode(iterable):
    for key, group in groupby(iterable):
        length = sum(1 for _ in group)
        yield key, length

if __name__ == '__main__':
    data = 'AAABBBCCCC'
    result = list(run_length_encode(data))
    print(result)