def rle_compress(data):
    if not data:
        return b''
    result = bytearray()
    current_byte = data[0]
    count = 1
    for i in range(1, len(data)):
        if data[i] == current_byte and count < 255:
            count += 1
        else:
            result.append(count)
            result.append(current_byte)
            current_byte = data[i]
            count = 1
    result.append(count)
    result.append(current_byte)
    return bytes(result)

if __name__ == '__main__':
    sample_data = b'AAABBBCCCDDDDDEEEE'
    compressed = rle_compress(sample_data)
    print(compressed)
    sample_data2 = b'\x00\x00\x00\x01\x01\x02'
    compressed2 = rle_compress(sample_data2)
    print(compressed2)
    sample_data3 = b''
    compressed3 = rle_compress(sample_data3)
    print(compressed3)
    sample_data4 = b'A'
    compressed4 = rle_compress(sample_data4)
    print(compressed4)