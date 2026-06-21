def encode_rle(data):
    if not data:
        return ""
    
    encoded = []
    current_char = data[0]
    count = 1
    
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            encoded.append(f"{current_char}{count}")
            current_char = data[i]
            count = 1
    
    encoded.append(f"{current_char}{count}")
    
    return "".join(encoded)

if __name__ == '__main__':
    sample_string = "aaabbbaaccccccc"
    result = encode_rle(sample_string)
    print(result)
    
    empty_string = ""
    empty_result = encode_rle(empty_string)
    print(empty_result)
    
    single_char = "z"
    single_result = encode_rle(single_char)
    print(single_result)
    
    no_repeat = "abcdef"
    no_repeat_result = encode_rle(no_repeat)
    print(no_repeat_result)