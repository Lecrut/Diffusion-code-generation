def bidirectional_rle(input_string):
    if not input_string:
        return ""
    
    compressed = []
    count = 1
    current_char = input_string[0]
    
    for i in range(1, len(input_string)):
        if input_string[i] == current_char:
            count += 1
        else:
            compressed.append(str(count) + current_char)
            current_char = input_string[i]
            count = 1
    compressed.append(str(count) + current_char)
    
    compressed_str = "".join(compressed)
    
    decompressed = []
    i = 0
    while i < len(compressed_str):
        num_str = ""
        while i < len(compressed_str) and compressed_str[i].isdigit():
            num_str += compressed_str[i]
            i += 1
        count = int(num_str)
        char = compressed_str[i]
        decompressed.append(char * count)
        i += 1
    
    decompressed_str = "".join(decompressed)
    return decompressed_str

if __name__ == '__main__':
    original = "AAAAABBBCCDE"
    result = bidirectional_rle(original)
    print(result)