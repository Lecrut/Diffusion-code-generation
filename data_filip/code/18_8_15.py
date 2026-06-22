def encode_rle(data: str) -> list:
    if not data:
        return []
    
    result = []
    current_char = data[0]
    count = 1
    
    for i in range(1, len(data)):
        char = data[i]
        if char == current_char:
            count += 1
        else:
            result.append(current_char)
            result.append(count)
            current_char = char
            count = 1
            
    result.append(current_char)
    result.append(count)
    
    return result

if __name__ == '__main__':
    input_string = "AAABBBCCC"
    encoded_output = encode_rle(input_string)
    print(encoded_output)