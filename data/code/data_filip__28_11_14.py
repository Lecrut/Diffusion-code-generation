def compress_binary_string(binary_string: str) -> str:
    if not binary_string:
        return ""
    
    if len(binary_string) == 1:
        return f"{binary_string[0]}1"
    
    result = []
    count = 1
    current_char = binary_string[0]
    
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
    test_cases = [
        "",
        "0",
        "1",
        "0000",
        "1111",
        "00110011",
        "10101010",
        "000111000"
    ]
    
    for test in test_cases:
        print(compress_binary_string(test))