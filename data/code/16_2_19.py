def run_length_encode(data):
    if not data:
        return []
    
    encoded = []
    current_value = data[0]
    current_count = 1
    
    for i in range(1, len(data)):
        byte = data[i]
        if byte == current_value:
            current_count += 1
        else:
            encoded.append((current_value, current_count))
            current_value = byte
            current_count = 1
    
    encoded.append((current_value, current_count))
    return encoded

if __name__ == '__main__':
    sample_data = b'AABBCCC'
    result = run_length_encode(sample_data)
    print(result)