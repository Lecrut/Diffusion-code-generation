def run_length_encode(data):
    if not data:
        return {}
    
    encoded_map = {}
    current_char = data[0]
    count = 1
    
    for i in range(1, len(data)):
        char = data[i]
        if char.isalnum() and char == current_char:
            count += 1
        else:
            if not current_char.isalnum():
                current_char = char
                count = 1
            else:
                encoded_map[current_char] = count
                current_char = char
                count = 1
    
    if current_char.isalnum():
        encoded_map[current_char] = count
        
    return encoded_map

if __name__ == '__main__':
    sample_data = "AAABBBCCCDa"
    result = run_length_encode(sample_data)
    print(result)