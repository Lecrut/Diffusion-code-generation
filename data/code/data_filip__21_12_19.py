import array

def run_length_encode(data: bytes) -> bytes:
    if len(data) == 0:
        return b''
    
    output = array.array('B')
    current_byte = data[0]
    count = 1
    
    for i in range(1, len(data)):
        byte = data[i]
        if byte == current_byte and count < 255:
            count += 1
        else:
            output.append(count)
            output.append(current_byte)
            current_byte = byte
            count = 1
    
    output.append(count)
    output.append(current_byte)
    
    return output.tobytes()

if __name__ == '__main__':
    sample_data = b'AAABBBBCCCCDDDDDDDE'
    encoded_result = run_length_encode(sample_data)
    print(encoded_result)