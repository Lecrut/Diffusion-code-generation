from itertools import groupby

def rle_encode(iterable):
    for key, group in groupby(iterable):
        yield (key, len(list(group)))

if __name__ == '__main__':
    data = 'AAABBBCCCC'
    result = list(rle_encode(data))
    print(result)