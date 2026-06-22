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
    sample1 = "aabcccccaaa"
    print(compress_rle(sample1))
    
    sample2 = "abcdef"
    print(compress_rle(sample2))
    
    sample3 = "aabbcc"
    print(compress_rle(sample3))
    
    sample4 = "aaaaa"
    print(compress_rle(sample4))
    
    sample5 = ""
    print(compress_rle(sample5))
    
    sample6 = "a"
    print(compress_rle(sample6))