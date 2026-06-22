def rle_encode(input_str):
    if not input_str:
        return ''
    
    result = []
    current_char = input_str[0]
    count = 1
    
    for i in range(1, len(input_str)):
        char = input_str[i]
        if char == current_char:
            count += 1
        else:
            if count > 1:
                result.append(f"{count}{current_char}")
            else:
                result.append(current_char)
            current_char = char
            count = 1
    
    if count > 1:
        result.append(f"{count}{current_char}")
    else:
        result.append(current_char)
    
    return ''.join(result)

if __name__ == '__main__':
    print(rle_encode('aabcccccaaa'))
    print(rle_encode('abc'))
    print(rle_encode('aabbcc'))
    print(rle_encode(''))
    print(rle_encode('aaaaaaaaaa'))