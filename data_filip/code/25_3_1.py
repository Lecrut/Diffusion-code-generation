def rle_encode(input_string):
    if not input_string:
        return ""
    
    encoded = []
    current_char = input_string[0]
    count = 1
    
    for i in range(1, len(input_string)):
        char = input_string[i]
        if char == current_char:
            count += 1
        else:
            encoded.append(f"{count}{current_char}")
            current_char = char
            count = 1
    
    encoded.append(f"{count}{current_char}")
    
    return "".join(encoded)

if __name__ == '__main__':
    text = "AAAABBBCCDAA"
    result = rle_encode(text)
    print(result)