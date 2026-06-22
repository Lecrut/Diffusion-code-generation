def rle_compress(data):
    if not data:
        return b''
    result = bytearray()
    count = 1
    for i in range(1, len(data)):
        if data[i] == data[i - 1] and count < 255:
            count += 1
        else:
            result.append(count)
            result.append(data[i - 1])
            count = 1
    result.append(count)
    result.append(data[-1])
    return bytes(result)

if __name__ == '__main__':
    sample_data = b'A' * 10 + b'B' * 5 + b'C'
    compressed = rle_compress(sample_data)
    print(compressed)