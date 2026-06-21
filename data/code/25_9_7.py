def rle_encode(data):
    if not data:
        return ""
    
    result = []
    current_char = data[0]
    count = 1
    
    for i in range(1, len(data)):
        char = data[i]
        if char == current_char:
            count += 1
        else:
            if count > 3:
                result.append(f"{count}{current_char}")
            elif count > 1:
                result.append(f"{current_char}{current_char}")
                result.append(current_char)
            else:
                result.append(current_char)
            current_char = char
            count = 1
            
    if count > 3:
        result.append(f"{count}{current_char}")
    elif count > 1:
        result.append(f"{current_char}{current_char}")
        result.append(current_char)
    else:
        result.append(current_char)
        
    return "".join(result)

if __name__ == '__main__':
    sample_input = "AAABBBCCCA"
    encoded = rle_encode(sample_input)
    print(encoded)