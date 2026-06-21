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

def rle_decode(data):
    if not data:
        return ''
    decoded = []
    i = 0
    while i < len(data):
        if data[i].isdigit():
            count = 0
            while i < len(data) and data[i].isdigit():
                count = count * 10 + int(data[i])
                i += 1
            if i < len(data):
                decoded.append(data[i] * count)
                i += 1
        else:
            decoded.append(data[i])
            i += 1
    return ''.join(decoded)

if __name__ == '__main__':
    sample_inputs = [
        ('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB', '12W1B12W3B24W1B'),
        ('AABCCCDEDD', '2ABC2DE2D'),
        ('ABC', 'ABC'),
        ('AAAAA', '5A'),
        ('', ''),
        ('X', 'X')
    ]
    
    for original, expected_encoded in sample_inputs:
        encoded = rle_encode(original)
        decoded = rle_decode(encoded)
        print(f"Original: {original!r}")
        print(f"Encoded: {encoded!r}")
        print(f"Expected Encoded: {expected_encoded!r}")
        print(f"Match: {encoded == expected_encoded}")
        print(f"Decoded: {decoded!r}")
        print(f"Round-trip Match: {decoded == original}")
        print()