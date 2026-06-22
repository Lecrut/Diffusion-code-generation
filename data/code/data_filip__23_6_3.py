import struct

def run_length_encode(data):
    if not data:
        return b''
    result = bytearray()
    count = 1
    current_byte = data[0]
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
    sample_data = bytearray([0, 0, 0, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3])
    encoded_result = run_length_encode(sample_data)
    print(encoded_result)