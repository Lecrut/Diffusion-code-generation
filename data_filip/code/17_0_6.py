def encode_rle(input_string):
    if not input_string:
        return ""
    
    encoded_parts = []
    current_char = input_string[0]
    count = 1
    
    for i in range(1, len(input_string)):
        if input_string[i] == current_char:
            count += 1
        else:
            encoded_parts.append(f"{current_char}{count}")
            current_char = input_string[i]
            count = 1
    
    encoded_parts.append(f"{current_char}{count}")
    
    return "".join(encoded_parts)

if __name__ == '__main__':
    sample_data = "AAABBCDDDD"
    result = encode_rle(sample_data)
    print(result)
    
    another_sample = "ZZZZZZZZZZ"
    print(encode_rle(another_sample))
    
    empty_sample = ""
    print(encode_rle(empty_sample))
    
    single_char = "A"
    print(encode_rle(single_char))