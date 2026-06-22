def run_length_encode(data):
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
    sample1 = b'AAABBBCCD'
    sample2 = b'abcde'
    sample3 = b''
    sample4 = b'\x00\x00\x00\xff\xff\x00\x00'
    print(run_length_encode(sample1))
    print(run_length_encode(sample2))
    print(run_length_encode(sample3))
    print(run_length_encode(sample4))