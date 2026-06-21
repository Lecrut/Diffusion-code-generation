def rle_encode(data):
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
            result.append(str(count) + current_char)
            current_char = char
            count = 1
    
    result.append(str(count) + current_char)
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbbcccd"
    encoded_output = rle_encode(sample_input)
    print(encoded_output)