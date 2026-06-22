def run_length_encode(data: bytes) -> bytes:
    if not data:
        return b''
    
    encoded_parts = []
    current_byte = data[0]
    count = 1
    
    for i in range(1, len(data)):
        if data[i] == current_byte:
            count += 1
        else:
            if count < 128:
                encoded_parts.append((count).to_bytes(1, 'big'))
                encoded_parts.append(bytes([current_byte]))
            else:
                encoded_parts.append(b'\x80')
                encoded_parts.append(count.to_bytes(2, 'big'))
                encoded_parts.append(bytes([current_byte]))
            current_byte = data[i]
            count = 1
    
    if count < 128:
        encoded_parts.append((count).to_bytes(1, 'big'))
        encoded_parts.append(bytes([current_byte]))
    else:
        encoded_parts.append(b'\x80')
        encoded_parts.append(count.to_bytes(2, 'big'))
        encoded_parts.append(bytes([current_byte]))
    
    return b''.join(encoded_parts)

if __name__ == '__main__':
    sample_input = b'AAABBBCCD'
    result = run_length_encode(sample_input)
    print(result)
    
    sample_input2 = b''
    result2 = run_length_encode(sample_input2)
    print(result2)
    
    sample_input3 = b'AAAAABBBCCDDDDDDD'
    result3 = run_length_encode(sample_input3)
    print(result3)