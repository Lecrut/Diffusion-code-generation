def rle_encode(text):
    if not text:
        return ""
    
    result = []
    current_char = text[0]
    count = 1
    
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            if count > 1:
                result.append(str(count))
            result.append(current_char)
            current_char = char
            count = 1
    
    if count > 1:
        result.append(str(count))
    result.append(current_char)
    
    return "".join(result)

def rle_decode(text):
    if not text:
        return ""
    
    result = []
    count_str = []
    
    for char in text:
        if char.isdigit():
            count_str.append(char)
        else:
            if count_str:
                count = int("".join(count_str))
                result.append(char * count)
                count_str = []
            else:
                result.append(char)
    
    return "".join(result)

if __name__ == '__main__':
    original = "aaaabbbccddeeeee"
    encoded = rle_encode(original)
    print(encoded)
    
    decoded = rle_decode(encoded)
    print(decoded)