def rle_encode(input_string):
    if not input_string:
        return ""
    
    result = []
    count = 1
    current_char = input_string[0]
    
    for i in range(1, len(input_string)):
        char = input_string[i]
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
    
    result.append(f"{count}{current_char}")
    return "".join(result)

def rle_decode(encoded_string):
    if not encoded_string:
        return ""
    
    result = []
    i = 0
    length = len(encoded_string)
    
    while i < length:
        count_str = []
        while i < length and encoded_string[i].isdigit():
            count_str.append(encoded_string[i])
            i += 1
        
        if not count_str:
            char = encoded_string[i]
            count = 1
            i += 1
        else:
            char = encoded_string[i]
            count = int("".join(count_str))
            i += 1
        
        result.append(char * count)
    
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbc"
    encoded = rle_encode(sample_input)
    print(encoded)
    
    decoded = rle_decode(encoded)
    print(decoded)