def rle_compress(data):
    if not data:
        return b''
    result = bytearray()
    length = len(data)
    i = 0
    while i < length:
        current_byte = data[i]
        count = 1
        while i + count < length and data[i + count] == current_byte and count < 255:
            count += 1
        result.append(count)
        result.append(current_byte)
        i += count
    return bytes(result)

if __name__ == '__main__':
    sample_data = b'AAABBBCCCCCDDEEEE'
    compressed = rle_compress(sample_data)
    print(compressed)
    sample_data2 = b'\x00\x00\x00\x01\x01\x02'
    compressed2 = rle_compress(sample_data2)
    print(compressed2)
    sample_data3 = b''
    compressed3 = rle_compress(sample_data3)
    print(compressed3)
    sample_data4 = b'\xff\x00\xff\x00'
    compressed4 = rle_compress(sample_data4)
    print(compressed4)