def rle_encode(input_string):
    if not input_string:
        return ""
    
    result = []
    current_char = input_string[0]
    count = 1
    
    for i in range(1, len(input_string)):
        char = input_string[i]
        if char == current_char:
            count += 1
        else:
            result.append(str(count) + current_char)
            current_char = char
            count = 1
    
    result.append(str(count) + current_char)
    
    return "".join(result)

if __name__ == '__main__':
    input_str = "aaabbc"
    encoded = rle_encode(input_str)
    print(encoded)