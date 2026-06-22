def encode_rle(input_string):
    if not input_string:
        return []
    
    result = []
    current_char = input_string[0]
    count = 1
    
    for i in range(1, len(input_string)):
        char = input_string[i]
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
    sample_string = "aaabbc"
    encoded = encode_rle(sample_string)
    print(encoded)