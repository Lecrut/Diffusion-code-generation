def decode_rle(s):
    if not s:
        return ""
    result = []
    current_num = []
    for char in s:
        if char.isdigit():
            current_num.append(char)
        else:
            if current_num:
                repeat_count = int(''.join(current_num))
                result.append(char * repeat_count)
                current_num = []
            else:
                result.append(char)
    return ''.join(result)

if __name__ == '__main__':
    compressed_string = "3A4B2C"
    decoded_string = decode_rle(compressed_string)
    print(decoded_string)