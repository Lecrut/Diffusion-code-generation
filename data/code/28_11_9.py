def run_length_encode(binary_string: str) -> str:
    if not binary_string:
        return ""
    
    if len(binary_string) == 1:
        return "1" + binary_string
    
    result = []
    count = 1
    current_char = binary_string[0]
    
    for i in range(1, len(binary_string)):
        char = binary_string[i]
        if char == current_char:
            count += 1
        else:
            result.append(str(count) + current_char)
            current_char = char
            count = 1
    
    result.append(str(count) + current_char)
    
    return "".join(result)

if __name__ == '__main__':
    print(run_length_encode(""))
    print(run_length_encode("0"))
    print(run_length_encode("1"))
    print(run_length_encode("00001110"))
    print(run_length_encode("10101010"))