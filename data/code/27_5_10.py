def rle_encode(input_string):
    if not input_string:
        return ""
    
    encoded = []
    shifted = ' ' + input_string
    
    for char, prev_char in zip(input_string, shifted):
        if char != prev_char:
            encoded.append(char)
            
    count = []
    current_count = 0
    last_char = ''
    
    for char in input_string:
        if char == last_char:
            current_count += 1
        else:
            if last_char:
                count.append(str(current_count))
            current_count = 1
            last_char = char
            
    if last_char:
        count.append(str(current_count))
        
    result = ''.join(c + n for c, n in zip(encoded, count))
    return result

if __name__ == '__main__':
    sample_input = 'AAAAABBBB'
    result = rle_encode(sample_input)
    print(result)