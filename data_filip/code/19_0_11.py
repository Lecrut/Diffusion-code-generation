def compress_rle(input_string):
    if not input_string:
        return ""
    
    compressed_parts = []
    current_char = input_string[0]
    count = 1
    
    for i in range(1, len(input_string)):
        char = input_string[i]
        if char == current_char:
            count += 1
        else:
            compressed_parts.append(str(count) + current_char)
            current_char = char
            count = 1
    
    compressed_parts.append(str(count) + current_char)
    
    return "".join(compressed_parts)

if __name__ == '__main__':
    sample_input_1 = "aaabbcdddd"
    sample_input_2 = "a"
    sample_input_3 = "abcd"
    sample_input_4 = ""
    
    result_1 = compress_rle(sample_input_1)
    result_2 = compress_rle(sample_input_2)
    result_3 = compress_rle(sample_input_3)
    result_4 = compress_rle(sample_input_4)
    
    print(result_1)
    print(result_2)
    print(result_3)
    print(result_4)