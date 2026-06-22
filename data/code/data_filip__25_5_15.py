import itertools

def rle_encode(s: str) -> list:
    encoded = []
    for key, group in itertools.groupby(s):
        count = sum(1 for _ in group)
        encoded.append((key, count))
    return encoded

def rle_decode(encoded: list) -> str:
    decoded = []
    for key, count in encoded:
        decoded.append(key * count)
    return "".join(decoded)

if __name__ == '__main__':
    original = "AAABBBCCD"
    encoded = rle_encode(original)
    print(encoded)
    decoded = rle_decode(encoded)
    print(decoded)