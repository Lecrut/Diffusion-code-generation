def rle_compress(data):
    if not data:
        return b''

    result = bytearray()
    i = 0
    while i < len(data):
        current_byte = data[i]
        count = 1
        while i + count < len(data) and data[i + count] == current_byte and count < 255:
            count += 1
        result.append(count)
        result.append(current_byte)
        i += count

    return bytes(result)

if __name__ == '__main__':
    sample_data = b'AAAAABBBCCCCDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDEEEEE'
    compressed = rle_compress(sample_data)
    print(compressed)
    sample_empty = b''
    print(rle_compress(sample_empty))
    sample_single = b'Z'
    print(rle_compress(sample_single))