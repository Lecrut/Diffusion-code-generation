def rle_encode(input_string):
    if not input_string:
        return ""
    
    encoded_chars = []
    index = 0
    length = len(input_string)
    
    while index < length:
        current_char = input_string[index]
        count = 1
        next_index = index + 1
        
        while next_index < length and input_string[next_index] == current_char:
            count += 1
            next_index += 1
        
        encoded_chars.append(str(count) + current_char)
        index = next_index
    
    return "".join(encoded_chars)

if __name__ == '__main__':
    print(rle_encode('AABBCC'))