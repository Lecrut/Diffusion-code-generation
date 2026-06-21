def run_length_compress(char_list):
    if not char_list:
        return []
    
    result = []
    current_char = char_list[0]
    count = 1
    
    for i in range(1, len(char_list)):
        char = char_list[i]
        if char == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = char
            count = 1
    
    result.append((current_char, count))
    
    return result

if __name__ == '__main__':
    sample_data = list("aaabbc")
    compressed = run_length_compress(sample_data)
    print(compressed)