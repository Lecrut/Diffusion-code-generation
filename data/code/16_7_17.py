def rle_encode(binary_string):
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
    binary_input = "1100011110000001"
    result = rle_encode(binary_input)
    print(result)