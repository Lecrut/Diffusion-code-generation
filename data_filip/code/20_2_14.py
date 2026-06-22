def compress_run_length_encoding(binary_sequence):
    if not binary_sequence:
        return ""
    
    result = []
    current_bit = binary_sequence[0]
    count = 1
    
    for i in range(1, len(binary_sequence)):
        bit = binary_sequence[i]
        if bit == current_bit:
            count += 1
        else:
            result.append(f"{current_bit}{count}")
            current_bit = bit
            count = 1
    
    result.append(f"{current_bit}{count}")
    
    return "".join(result)

if __name__ == '__main__':
    binary_sequence = "11100011101"
    compressed = compress_run_length_encoding(binary_sequence)
    print(compressed)