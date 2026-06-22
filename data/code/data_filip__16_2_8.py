def run_length_encode(data: bytes) -> list:
    if not data:
        return []
    
    encoded_list = []
    current_byte = data[0]
    count = 1
    
    for i in range(1, len(data)):
        if data[i] == current_byte:
            count += 1
        else:
            encoded_list.append((current_byte, count))
            current_byte = data[i]
            count = 1
    
    encoded_list.append((current_byte, count))
    return encoded_list

if __name__ == '__main__':
    sample_data = b'AAAABBBCCDAA'
    result = run_length_encode(sample_data)
    print(result)