def rle_compress(data):
    if not data:
        return b''
    result = bytearray()
    i = 0
    n = len(data)
    while i < n:
        current_byte = data[i]
        count = 1
        while i + count < n and data[i + count] == current_byte and count < 255:
            count += 1
        if count > 1:
            result.append(count)
            result.append(current_byte)
        else:
            result.append(current_byte)
        i += count
    return bytes(result)

if __name__ == '__main__':
    sample_data = b'AAABBBCCCCDDDDDD'
    compressed = rle_compress(sample_data)
    print(compressed)