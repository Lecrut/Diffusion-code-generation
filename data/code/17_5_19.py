def rle_encode(input_string):
    if not input_string:
        return ""
    
    encoded = []
    current_char = input_string[0]
    count = 1
    
    for char in input_string[1:]:
        if char == current_char:
            count += 1
        else:
            if count > 1:
                encoded.append(str(count))
            encoded.append(current_char)
            current_char = char
            count = 1
    
    if count > 1:
        encoded.append(str(count))
    encoded.append(current_char)
    
    return ''.join(encoded)

if __name__ == '__main__':
    sample_strings = [
        "AAABBBCCD",
        "ABC",
        "AAAAAAAA",
        "AABBCC",
        "XYZZZZ",
        "",
        "A"
    ]
    
    for s in sample_strings:
        print(rle_encode(s))