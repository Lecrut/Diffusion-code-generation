def run_length_encode(byte_sequence):
    if not byte_sequence:
        return []
    
    result = []
    current_value = byte_sequence[0]
    count = 1
    
    for byte_value in byte_sequence[1:]:
        if byte_value == current_value:
            count += 1
        else:
            result.append((current_value, count))
            current_value = byte_value
            count = 1
    
    result.append((current_value, count))
    return result

if __name__ == '__main__':
    sample_data = bytes([65, 65, 65, 66, 66, 67, 67, 67, 67, 65])
    encoded = run_length_encode(sample_data)
    print(encoded)