def rle_encode(text):
    if not text:
        return ""
    
    result = []
    current_char = text[0]
    count = 1
    
    for i in range(1, len(text)):
        char = text[i]
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
    
    result.append(f"{count}{current_char}")
    return "".join(result)

if __name__ == '__main__':
    input_string = "AAABBBCCD"
    encoded = rle_encode(input_string)
    print(encoded)