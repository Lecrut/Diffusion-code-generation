def rle_encode(data):
    if not data:
        return
    current = data[0]
    count = 1
    for item in data[1:]:
        if item == current:
            count += 1
        else:
            yield (current, count)
            current = item
            count = 1
    yield (current, count)

def rle_decode(encoded):
    for value, count in encoded:
        for _ in range(count):
            yield value

if __name__ == '__main__':
    sample = 'AAABBBCCCDAA'
    encoded = list(rle_encode(sample))
    print(encoded)
    decoded = ''.join(rle_decode(encoded))
    print(decoded)