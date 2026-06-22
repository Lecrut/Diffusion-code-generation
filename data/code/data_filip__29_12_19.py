def encode_repeated_chars(input_string):
    if not input_string:
        return []
    
    segments = []
    current_char = input_string[0]
    count = 1
    
    for char in input_string[1:]:
        if char == current_char:
            count += 1
        else:
            if count > 1:
                encoded = f"{current_char}{count}"
                segments.append(encoded)
                current_char = char
                count = 1
            else:
                current_char = char
                count = 1
    
    if count > 1:
        encoded = f"{current_string[0]}{count}"
        segments.append(encoded)
    
    return segments

if __name__ == '__main__':
    test_string = "aaabbc"
    result = encode_repeated_chars(test_string)
    print(result)