def run_length_encode_binary(binary_string):
    counts = []
    current_count = 0
    if not binary_string:
        return counts
    current_bit = binary_string[0]
    for bit in binary_string:
        if bit == current_bit:
            current_count += 1
        else:
            counts.append(current_count)
            current_count = 1
            current_bit = bit
    counts.append(current_count)
    return counts

if __name__ == '__main__':
    sample_binary = "1110011110"
    result = run_length_encode_binary(sample_binary)
    print(result)