def rle_encode(data: str) -> str:
    if not data:
        return ""
    
    result = []
    current_char = data[0]
    count = 1
    
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = data[i]
            count = 1
    
    result.append(f"{current_char}{count}")
    
    return "".join(result)

if __name__ == '__main__':
    sample_string = "aaabbcdddd"
    encoded_result = rle_encode(sample_string)
    print(encoded_result)
    
    empty_string = ""
    empty_result = rle_encode(empty_string)
    print(empty_result)
    
    single_char = "x"
    single_result = rle_encode(single_char)
    print(single_result)
    
    mixed_string = "aA11"
    mixed_result = rle_encode(mixed_string)
    print(mixed_result)