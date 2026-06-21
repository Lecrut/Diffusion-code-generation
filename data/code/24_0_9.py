def compress_rle(data: str) -> str:
    if not data:
        return ""
    
    result = []
    current_char = data[0]
    count = 1
    length = len(data)
    
    for i in range(1, length):
        char = data[i]
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
            
    result.append(f"{count}{current_char}")
    return "".join(result)

if __name__ == '__main__':
    input_string = "AAABBBCCCD"
    compressed = compress_rle(input_string)
    print(compressed)