def encode_rle(s):
    if not s:
        return []
    result = []
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            result.append((count, current_char))
            current_char = char
            count = 1
    result.append((count, current_char))
    return result

if __name__ == '__main__':
    sample_input = "aaabbccccd"
    encoded_result = encode_rle(sample_input)
    print(encoded_result)
    
    empty_input = ""
    empty_result = encode_rle(empty_input)
    print(empty_result)
    
    single_char = "z"
    single_result = encode_rle(single_char)
    print(single_result)
    
    mixed_input = "11100022"
    mixed_result = encode_rle(mixed_input)
    print(mixed_result)