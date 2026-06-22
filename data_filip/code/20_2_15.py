def compress_rle(data):
    if not data:
        return []
    compressed = []
    count = 1
    current_byte = data[0]
    for i in range(1, len(data)):
        if data[i] == current_byte:
            count += 1
        else:
            compressed.append((current_byte, count))
            current_byte = data[i]
            count = 1
    compressed.append((current_byte, count))
    return compressed

if __name__ == '__main__':
    sample_data = bytes([0x00, 0x00, 0x00, 0x01, 0x01, 0x02, 0x02, 0x02, 0x02])
    result = compress_rle(sample_data)
    print(result)