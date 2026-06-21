def rle_encode(data):
    if not data:
        return ""
    
    encoded = []
    current_char = data[0]
    count = 1
    
    for i in range(1, len(data)):
        char = data[i]
        if char == current_char:
            count += 1
        else:
            encoded.append(str(count) + current_char)
            current_char = char
            count = 1
    
    encoded.append(str(count) + current_char)
    return "".join(encoded)

if __name__ == '__main__':
    text = "aaabbbcc"
    result = rle_encode(text)
    print(result)