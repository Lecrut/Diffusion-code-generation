from itertools import groupby

def rle_encode(data):
    if not data:
        return ()
    return tuple((k, len(list(g))) for k, g in groupby(data))

if __name__ == '__main__':
    sample_input = "AAABBC"
    result = rle_encode(sample_input)
    print(result)