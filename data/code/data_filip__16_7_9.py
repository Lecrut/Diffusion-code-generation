def run_length_encode(binary_string):
    if not binary_string:
        return []
    counts = []
    current_char = binary_string[0]
    count = 1
    for i in range(1, len(binary_string)):
        char = binary_string[i]
        if char == current_char:
            count += 1
        else:
            counts.append(count)
            current_char = char
            count = 1
    counts.append(count)
    return counts

if __name__ == '__main__':
    binary_str = "111000001111111001"
    result = run_length_encode(binary_str)
    print(result)