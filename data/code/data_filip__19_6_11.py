def rle_encode_lowercase(data: str) -> str:
    if not data:
        return ""
    
    result = []
    lower_data = data.lower()
    current_char = lower_data[0]
    count = 1
    
    for i in range(1, len(lower_data)):
        char = lower_data[i]
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
    
    result.append(f"{count}{current_char}")
    return "".join(result)

if __name__ == '__main__':
    print(rle_encode_lowercase("AaAABbcCDDD"))