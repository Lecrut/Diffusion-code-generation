def run_length_encode(byte_sequence):
    if not byte_sequence:
        return []
    
    result = []
    current_byte = byte_sequence[0]
    count = 1
    
    for i in range(1, len(byte_sequence)):
        byte = byte_sequence[i]
        if byte == current_byte:
            count += 1
        else:
            result.append((current_byte, count))
            current_byte = byte
            count = 1
    
    result.append((current_byte, count))
    return result

if __name__ == '__main__':
    sample = b'AABBBCCCC'
    print(run_length_encode(sample))