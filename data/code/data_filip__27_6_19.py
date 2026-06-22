def rle_encode(input_string):
    if not input_string:
        return []
    
    result = []
    current_byte = input_string[0].encode('utf-8')[0]
    count = 1
    
    for i in range(1, len(input_string)):
        next_byte = input_string[i].encode('utf-8')[0]
        if next_byte == current_byte and count < 255:
            count += 1
        else:
            result.append((chr(current_byte), count))
            current_byte = next_byte
            count = 1
    
    result.append((chr(current_byte), count))
    return result

if __name__ == '__main__':
    sample_string = "AAABBBCCDAA"
    encoded = rle_encode(sample_string)
    print(encoded)