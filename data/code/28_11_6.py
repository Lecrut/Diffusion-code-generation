def compress_binary_string(binary_string: str) -> str:
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
    test_cases = ["", "1", "0001110", "11111", "010101", "101000111100"]
    for test in test_cases:
        print(compress_binary_string(test))