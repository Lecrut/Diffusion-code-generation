def run_length_encode(binary_string):
    if not binary_string:
        return ""
    
    if len(binary_string) == 1:
        return "1" + binary_string
    
    result = []
    current_char = binary_string[0]
    count = 1
    
    for i in range(1, len(binary_string)):
        if binary_string[i] == current_char:
            count += 1
        else:
            result.append(str(count))
            result.append(current_char)
            current_char = binary_string[i]
            count = 1
    
    result.append(str(count))
    result.append(current_char)
    
    return "".join(result)

if __name__ == '__main__':
    test_cases = [
        "",
        "0",
        "1",
        "0011101111",
        "11111111",
        "0000"
    ]
    
    for case in test_cases:
        encoded = run_length_encode(case)
        print(encoded)