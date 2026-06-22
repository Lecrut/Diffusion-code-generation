def encode(text):
    if not text:
        return ''
    
    result = []
    current_char = text[0]
    count = 1
    
    for i in range(1, len(text)):
        char = text[i]
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
    
    return ''.join(result)

def decode(encoded_text):
    if not encoded_text:
        return ''
    
    result = []
    current_count_str = []
    
    for char in encoded_text:
        if char.isdigit():
            current_count_str.append(char)
        else:
            if current_count_str:
                count = int(''.join(current_count_str))
                result.append(char * count)
                current_count_str = []
            else:
                result.append(char)
    
    return ''.join(result)

if __name__ == '__main__':
    print(encode('aaaabbbcc'))
    print(decode('4a3b2c'))
    print(encode('xyz'))
    print(decode('xyz'))
    print(encode('a1b2c3'))
    print(decode('a1b2c3'))
    print(encode(''))
    print(decode(''))
    print(encode('aaabbbcccdddd'))
    print(decode('3a3b3c4d'))