def rle_compress(s: str) -> str:
    if not s:
        return ""
    
    if len(s) == 1:
        return "1" + s
    
    result = []
    current_char = s[0]
    count = 1
    
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(str(count))
            result.append(current_char)
            current_char = char
            count = 1
            
    result.append(str(count))
    result.append(current_char)
    
    return "".join(result)

if __name__ == '__main__':
    test_string = "aaabbc"
    compressed = rle_compress(test_string)
    print(compressed)
    
    empty_string = ""
    empty_compressed = rle_compress(empty_string)
    print(empty_compressed)
    
    single_string = "z"
    single_compressed = rle_compress(single_string)
    print(single_compressed)
    
    long_run = "wwwwwwwwwwwwwwwaaaaaaabbbbb"
    long_compressed = rle_compress(long_run)
    print(long_compressed)
    
    no_run = "abcdef"
    no_run_compressed = rle_compress(no_run)
    print(no_run_compressed)