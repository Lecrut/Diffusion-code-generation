def run_length_encode(binary_string):
    if not binary_string:
        return []
    result = []
    current_char = binary_string[0]
    count = 1
    for char in binary_string[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(count)
            current_char = char
            count = 1
    result.append(count)
    return result

if __name__ == '__main__':
    sample_input = "1100011110"
    encoded_result = run_length_encode(sample_input)
    print(encoded_result)