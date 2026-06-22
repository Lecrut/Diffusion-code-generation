def compress_string(input_str):
    if not input_str:
        return ""
    
    compressed = []
    count = 1
    current_char = input_str[0]
    
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
    sample_1 = "aaabbccccd"
    sample_2 = "abcdef"
    sample_3 = ""
    sample_4 = "a"
    sample_5 = "wwwwaaadexxxxxxwww"
    
    print(compress_string(sample_1))
    print(compress_string(sample_2))
    print(compress_string(sample_3))
    print(compress_string(sample_4))
    print(compress_string(sample_5))