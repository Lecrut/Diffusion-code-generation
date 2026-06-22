def run_length_encode(binary_string):
    if not binary_string:
        return []
    
    result = []
    count = 0
    current_bit = binary_string[0]
    
    for bit in binary_string:
        if bit == current_bit:
            count += 1
        else:
            result.append(count)
            current_bit = bit
            count = 1
    result.append(count)
    return result

if __name__ == '__main__':
    binary_input = "11100111110000"
    encoded_counts = run_length_encode(binary_input)
    print(encoded_counts)