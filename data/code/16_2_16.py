def run_length_encode(data):
    if not data:
        return []
    
    result = []
    current_byte = data[0]
    count = 1
    
    for i in range(1, len(data)):
        byte = data[i]
        if byte == current_byte:
            count += 1
        else:
            result.append((current_byte, count))
            current_byte = byte
            count = 1
    
    result.append((current_byte, count))
    
    return result

if __name__ == '__main__':
    sample_bytes = b'AABBCCCDDDD'
    encoded = run_length_encode(sample_bytes)
    print(encoded)