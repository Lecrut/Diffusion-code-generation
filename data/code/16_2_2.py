def run_length_encode(data):
    if not data:
        return []
    
    encoded = []
    current_byte = data[0]
    count = 1
    
    for i in range(1, len(data)):
        byte = data[i]
        if byte == current_byte:
            count += 1
        else:
            encoded.append((current_byte, count))
            current_byte = byte
            count = 1
    
    encoded.append((current_byte, count))
    
    return encoded

if __name__ == '__main__':
    sample_data = b'AABBBCCCC'
    result = run_length_encode(sample_data)
    print(result)