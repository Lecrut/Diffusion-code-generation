from itertools import groupby

def rle_encode(iterable):
    for key, group in groupby(iterable):
        count = sum(1 for _ in group)
        yield (key, count)

if __name__ == '__main__':
    data = 'AAABBBCCCC'
    result = list(rle_encode(data))
    print(result)