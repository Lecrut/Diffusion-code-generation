def run_length_encode(binary_str):
    if not binary_str:
        return []
    
    counts = []
    current_char = binary_str[0]
    current_count = 1
    
    for char in binary_str[1:]:
        if char == current_char:
            current_count += 1
        else:
            counts.append(current_count)
            current_char = char
            current_count = 1
    
    counts.append(current_count)
    return counts

if __name__ == '__main__':
    binary_string = "11100011"
    result = run_length_encode(binary_string)
    print(result)