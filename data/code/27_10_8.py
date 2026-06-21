def compress_string(data):
    if not data:
        return ''
    
    compressed = []
    current_char = data[0]
    count = 1
    
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            compressed.append(f"{current_char}{count}")
            current_char = data[i]
            count = 1
    
    compressed.append(f"{current_char}{count}")
    return ''.join(compressed)

def decompress_string(data):
    if not data:
        return ''
    
    result = []
    i = 0
    
    while i < len(data):
        char = data[i]
        i += 1
        
        num_str = ''
        while i < len(data) and data[i].isdigit():
            num_str += data[i]
            i += 1
        
        if num_str:
            result.append(char * int(num_str))
        else:
            result.append(char)
    
    return ''.join(result)

if __name__ == '__main__':
    sample_input = "aaabbbccccdd"
    encoded = compress_string(sample_input)
    print(encoded)
    decoded = decompress_string(encoded)
    print(decoded)
    
    empty_test = compress_string("")
    print(empty_test)
    
    single_char = compress_string("z")
    print(single_char)
    
    mixed_input = "a1b2c3"
    encoded_mixed = compress_string(mixed_input)
    print(encoded_mixed)