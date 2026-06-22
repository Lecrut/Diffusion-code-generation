def rle_compress(data: bytes) -> bytes:
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
    sample_data = b'AAAABBBCCDAA'
    compressed = rle_compress(sample_data)
    print(compressed)
    
    empty_data = b''
    compressed_empty = rle_compress(empty_data)
    print(compressed_empty)
    
    single_byte = b'X'
    compressed_single = rle_compress(single_byte)
    print(compressed_single)
    
    no_repeats = b'ABCDEF'
    compressed_no_repeats = rle_compress(no_repeats)
    print(compressed_no_repeats)
    
    long_repeat = b'A' * 300
    compressed_long = rle_compress(long_repeat)
    print(compressed_long)