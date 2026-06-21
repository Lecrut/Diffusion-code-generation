import itertools

def rle_encode(iterable):
    for key, group in itertools.groupby(iterable):
        yield (key, sum(1 for _ in group))

if __name__ == '__main__':
    sample_string = 'AAABBBCCCC'
    result = list(rle_encode(sample_string))
    print(result)