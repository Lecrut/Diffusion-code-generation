def compress_binary_string(binary_string):
    if not binary_string:
        return ""
    
    result = []
    current_char = binary_string[0]
    count = 1
    
    for i in range(1, len(binary_string)):
        if binary_string[i] == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = binary_string[i]
            count = 1
    
    result.append(f"{current_char}{count}")
    return "".join(result)

if __name__ == '__main__':
    print(compress_binary_string(""))
    print(compress_binary_string("0"))
    print(compress_binary_string("1"))
    print(compress_binary_string("00001111"))
    print(compress_binary_string("010101"))
    print(compress_binary_string("111000011"))
    print(compress_binary_string("00000"))
    print(compress_binary_string("11111"))