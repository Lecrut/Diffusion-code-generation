from itertools import groupby

def rle_encode(data):
    return [(key, sum(1 for _ in group)) for key, group in groupby(data)]

def rle_decode(encoded_data):
    return [key * count for key, count in encoded_data]

if __name__ == '__main__':
    sample_input = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    encoded = rle_encode(sample_input)
    print(encoded)
    decoded = rle_decode(encoded)
    print("".join(decoded))