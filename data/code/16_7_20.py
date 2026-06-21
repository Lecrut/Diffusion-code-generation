def run_length_encode(binary_string):
    if not binary_string:
        return []
    counts = []
    current_count = 0
    current_bit = binary_string[0]
    for bit in binary_string:
        if bit == current_bit:
            current_count += 1
        else:
            counts.append(current_count)
            current_bit = bit
            current_count = 1
    counts.append(current_count)
    return counts

if __name__ == '__main__':
    binary_input = "111000011100011"
    result = run_length_encode(binary_input)
    print(result)