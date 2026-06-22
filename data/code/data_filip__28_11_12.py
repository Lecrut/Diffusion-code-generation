def compress_binary_string(binary_string):
    if not binary_string:
        return ""
    
    if len(binary_string) == 1:
        return f"{binary_string[0]}1"
    
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
    sample1 = "11100011"
    sample2 = "1"
    sample3 = ""
    sample4 = "00000"
    
    print(compress_binary_string(sample1))
    print(compress_binary_string(sample2))
    print(compress_binary_string(sample3))
    print(compress_binary_string(sample4))