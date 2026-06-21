def compress_rle(input_string):
    if not input_string:
        return ""
    
    compressed = []
    current_char = input_string[0]
    count = 1
    
    for char in input_string[1:]:
        if char == current_char:
            count += 1
        else:
            if count > 1:
                compressed.append(str(count))
            compressed.append(current_char)
            current_char = char
            count = 1
            
    if count > 1:
        compressed.append(str(count))
    compressed.append(current_char)
    
    return "".join(compressed)

if __name__ == '__main__':
    sample_inputs = [
        "AABCCCDDDD",
        "ABCDE",
        "AAAA",
        "ABABAB",
        "",
        "A",
        "AAABBCCCCCC"
    ]
    
    for sample in sample_inputs:
        result = compress_rle(sample)
        print(result)