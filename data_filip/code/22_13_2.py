def rle_compress(input_string):
    if not input_string:
        return ""
    
    result = []
    n = len(input_string)
    i = 0
    
    while i < n:
        current_char = input_string[i]
        count = 1
        while i + count < n and input_string[i + count] == current_char:
            count += 1
        
        if count >= 3:
            result.append(f"{current_char}{count}")
        else:
            result.append(current_char * count)
        
        i += count
    
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbbccddddeefgggg"
    compressed = rle_compress(sample_input)
    print(compressed)