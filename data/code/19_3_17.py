def rle_compress(data: bytes) -> bytes:
    if not data:
        return b''

    result = bytearray()
    current_byte = data[0]
    count = 1

    for i in range(1, len(data)):
        if data[i] == current_byte and count < 255:
            count += 1
        else:
            result.append(current_byte)
            result.append(count)
            current_byte = data[i]
            count = 1

    result.append(current_byte)
    result.append(count)

    return bytes(result)

if __name__ == '__main__':
    sample_data = b'AAABBBCCCCCCDD'
    compressed = rle_compress(sample_data)
    print(compressed)

    sample_empty = b''
    compressed_empty = rle_compress(sample_empty)
    print(compressed_empty)

    sample_single = b'\x00'
    compressed_single = rle_compress(sample_single)
    print(compressed_single)

    sample_repeated = b'\xff' * 300
    compressed_repeated = rle_compress(sample_repeated)
    print(compressed_repeated)