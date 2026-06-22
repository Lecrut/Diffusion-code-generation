def run_length_encode(binary_string):
    if not binary_string:
        return ""
    
    compressed = []
    current_char = binary_string[0]
    count = 1
    
    for i in range(1, len(binary_string)):
        if binary_string[i] == current_char:
            count += 1
        else:
            compressed.append(f"{current_char}{count}")
            current_char = binary_string[i]
            count = 1
    
    compressed.append(f"{current_char}{count}")
    return "".join(compressed)

if __name__ == '__main__':
    sample_empty = ""
    sample_single = "1"
    sample_normal = "1110001111"
    sample_alternating = "10101"
    
    print(run_length_encode(sample_empty))
    print(run_length_encode(sample_single))
    print(run_length_encode(sample_normal))
    print(run_length_encode(sample_alternating))