def run_length_encode(data: str) -> list:
    if not data:
        return []
    
    encoded_list = []
    current_char = data[0]
    count = 1
    
    for i in range(1, len(data)):
        char = data[i]
        if char == current_char:
            count += 1
        else:
            encoded_list.append((current_char, count))
            current_char = char
            count = 1
            
    encoded_list.append((current_char, count))
    return encoded_list

if __name__ == '__main__':
    sample_inputs = ["", "A", "AAABBC", "XYZ", ""]
    
    for s in sample_inputs:
        result = run_length_encode(s)
        print(result)