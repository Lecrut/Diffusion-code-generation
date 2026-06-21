def compress_string(input_str):
    if not input_str:
        return ""
    
    compressed = []
    current_char = input_str[0]
    count = 1
    
    for i in range(1, len(input_str)):
        if input_str[i] == current_char:
            count += 1
        else:
            compressed.append(current_char + str(count))
            current_char = input_str[i]
            count = 1
    
    compressed.append(current_char + str(count))
    
    return "".join(compressed)

if __name__ == '__main__':
    sample_input = 'aabcccccaaa'
    result = compress_string(sample_input)
    print(result)