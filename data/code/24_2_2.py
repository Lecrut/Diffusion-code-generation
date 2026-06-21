def rle_encode(data):
    if not data:
        return ''
    encoded = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            if count > 1:
                encoded.append(str(count))
            encoded.append(current_char)
            current_char = char
            count = 1
    if count > 1:
        encoded.append(str(count))
    encoded.append(current_char)
    return ''.join(encoded)

def rle_decode(encoded):
    decoded = []
    i = 0
    while i < len(encoded):
        if encoded[i].isdigit():
            count = int(encoded[i])
            i += 1
            while i < len(encoded) and encoded[i].isdigit():
                count = count * 10 + int(encoded[i])
                i += 1
            decoded.append(encoded[i] * count)
        else:
            decoded.append(encoded[i])
        i += 1
    return ''.join(decoded)

if __name__ == '__main__':
    samples = ['AAABBC', 'ABC', 'AABBCC', 'AAAAAAAA', 'ABABAB', '']
    for sample in samples:
        encoded = rle_encode(sample)
        decoded = rle_decode(encoded)
        print(repr(encoded), repr(decoded), sample == decoded)