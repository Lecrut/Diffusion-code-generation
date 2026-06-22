import itertools

def rle_encode(sequence):
    if not sequence:
        return {}
    encoded = {}
    for char, group in itertools.groupby(sequence):
        length = len(list(group))
        encoded[char] = length
    return encoded

if __name__ == '__main__':
    result = rle_encode("aaabbc")
    print(result)