def run_length_compress(char_list):
    if not char_list:
        return []
    
    result = []
    current_char = char_list[0]
    count = 1
    
    for i in range(1, len(char_list)):
        if char_list[i] == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = char_list[i]
            count = 1
            
    result.append((current_char, count))
    return result

if __name__ == '__main__':
    sample_data = ['A', 'A', 'B', 'B', 'B', 'C', 'D', 'D', 'D', 'D']
    compressed = run_length_compress(sample_data)
    print(compressed)