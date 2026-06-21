def rle_encode(input_string):
    if not input_string:
        return []
    
    encoded_list = []
    current_char = input_string[0]
    count = 1
    
    for i in range(1, len(input_string)):
        char = input_string[i]
        if char == current_char:
            count += 1
        else:
            encoded_list.append((current_char, count))
            current_char = char
            count = 1
            
    encoded_list.append((current_char, count))
    
    return encoded_list

if __name__ == '__main__':
    sample_text = "aaabbc"
    result = rle_encode(sample_text)
    print(result)