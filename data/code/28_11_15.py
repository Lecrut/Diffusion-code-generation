def rle_encode(binary_string):
    if not binary_string:
        return ""
    
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
    test_cases = ["", "1", "00000", "101010", "111000011111"]
    for case in test_cases:
        encoded = rle_encode(case)
        print(f"Input: '{case}' -> Output: '{encoded}'")