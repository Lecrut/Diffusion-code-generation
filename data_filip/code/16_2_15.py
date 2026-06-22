def run_length_encode(data: bytes) -> list:
    if not data:
        return []
    
    result = []
    current_byte = data[0]
    count = 1
    
    for i in range(1, len(data)):
        if data[i] == current_byte:
            count += 1
        else:
            result.append((current_byte, count))
            current_byte = data[i]
            count = 1
    
    result.append((current_byte, count))
    return result

if __name__ == '__main__':
    sample_data = b'aaabbcdddde'
    encoded = run_length_encode(sample_data)
    print(encoded)