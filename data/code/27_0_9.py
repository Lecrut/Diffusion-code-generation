def rle_encode(text):
    if not text:
        return []
    return [(char, len(list(group))) for char, group in __import__('itertools').groupby(text)]

if __name__ == '__main__':
    print(rle_encode("AAABBC"))