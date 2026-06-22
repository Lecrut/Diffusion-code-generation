def enhanced_rle_encode(data):
    if not data:
        return ""
    result = []
    i = 0
    n = len(data)
    while i < n:
        char = data[i]
        count = 1
        while i + count < n and data[i + count] == char and count < 99:
            count += 1
        if char == '\\':
            escaped_char = '\\\\'
            result.append(str(count) + escaped_char)
        elif char == '\n':
            escaped_char = '\\n'
            result.append(str(count) + escaped_char)
        elif char == '\t':
            escaped_char = '\\t'
            result.append(str(count) + escaped_char)
        elif char == '\r':
            escaped_char = '\\r'
            result.append(str(count) + escaped_char)
        elif ord(char) < 32 or ord(char) > 126:
            hex_code = format(ord(char), '02x')
            escaped_char = '\\x' + hex_code
            result.append(str(count) + escaped_char)
        else:
            if count > 1:
                result.append(str(count) + char)
            else:
                result.append(char)
        i += count
    return ''.join(result)

def enhanced_rle_decode(data):
    if not data:
        return ""
    result = []
    i = 0
    n = len(data)
    while i < n:
        char = data[i]
        if char == '\\':
            if i + 1 < n:
                next_char = data[i + 1]
                if next_char == '\\':
                    decoded_char = '\\'
                    i += 2
                elif next_char == 'n':
                    decoded_char = '\n'
                    i += 2
                elif next_char == 't':
                    decoded_char = '\t'
                    i += 2
                elif next_char == 'r':
                    decoded_char = '\r'
                    i += 2
                elif next_char == 'x' and i + 3 < n:
                    hex_str = data[i + 2:i + 4]
                    try:
                        decoded_char = chr(int(hex_str, 16))
                        i += 4
                    except ValueError:
                        decoded_char = data[i]
                        i += 1
                else:
                    decoded_char = char
                    i += 1
                if i < n and data[i].isdigit():
                    count_str = ""
                    while i < n and data[i].isdigit():
                        count_str += data[i]
                        i += 1
                    count = int(count_str) if count_str else 1
                    result.append(decoded_char * count)
                else:
                    result.append(decoded_char)
            else:
                result.append(char)
                i += 1
        else:
            count_str = ""
            while i < n and data[i].isdigit():
                count_str += data[i]
                i += 1
            if count_str:
                count = int(count_str)
            else:
                count = 1
                i -= len(count_str) if count_str else 0
            if i < n:
                current_char = data[i]
                result.append(current_char * count)
                i += 1
            else:
                break
    return ''.join(result)

if __name__ == '__main__':
    sample_data = "AABBBCCDDDDDE\\nTab\tHere"
    encoded = enhanced_rle_encode(sample_data)
    decoded = enhanced_rle_decode(encoded)
    print(encoded)
    print(decoded)
    print(sample_data == decoded)
    
    sample_data2 = "Hello World\\x20Test"
    encoded2 = enhanced_rle_encode(sample_data2)
    decoded2 = enhanced_rle_decode(encoded2)
    print(encoded2)
    print(decoded2)
    print(sample_data2 == decoded2)
    
    sample_data3 = "\\\\Backslash"
    encoded3 = enhanced_rle_encode(sample_data3)
    decoded3 = enhanced_rle_decode(encoded3)
    print(encoded3)
    print(decoded3)
    print(sample_data3 == decoded3)