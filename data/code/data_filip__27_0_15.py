def encode_rle(text):
    if not text:
        return []
    return [(char, len(list(group))) for char, group in __import__('itertools').groupby(text)]

if __name__ == '__main__':
    result = encode_rle("aaabbc")
    print(result)