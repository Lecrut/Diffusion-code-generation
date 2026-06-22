def run_length_encode(data):
    if not data:
        return b''
    if not isinstance(data, (bytes, bytearray)):
        raise TypeError("Input must be bytes or bytearray")
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
    sample1 = b'AAABBBCCD'
    print(run_length_encode(sample1))
    sample2 = b''
    print(run_length_encode(sample2))
    sample3 = b'\x00\x00\x00\xff\xff'
    print(run_length_encode(sample3))
    sample4 = b'ABCDEFGHIJ'
    print(run_length_encode(sample4))