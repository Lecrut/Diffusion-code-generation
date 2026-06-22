def compress_binary_string(binary_string):
    if not binary_string:
        return ""
    if len(binary_string) == 1:
        return binary_string
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
    test_cases = ["", "0", "1", "0001110", "11111111", "01010101", "001110001"]
    for case in test_cases:
        print(compress_binary_string(case))