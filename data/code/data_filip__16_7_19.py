def binary_to_run_length_encoded(binary_string):
    if not binary_string:
        return []
    counts = []
    current_char = binary_string[0]
    current_count = 1
    for char in binary_string[1:]:
        if char == current_char:
            current_count += 1
        else:
            counts.append(current_count)
            current_char = char
            current_count = 1
    counts.append(current_count)
    return counts

if __name__ == '__main__':
    binary_string = "1110001100111"
    result = binary_to_run_length_encoded(binary_string)
    print(result)