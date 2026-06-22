def bidirectional_rle(input_string):
    if not input_string:
        return {'original': '', 'compressed': '', 'decompressed': '', 'integrity_verified': True}
    compressed = []
    count = 0
    current_char = input_string[0]
    for char in input_string[1:]:
        if char == current_char:
            count += 1
        else:
            compressed.append(str(count) + current_char)
            current_char = char
            count = 1
    compressed.append(str(count) + current_char)
    compressed_str = ''.join(compressed)
    decompressed = []
    i = 0
    length = len(compressed_str)
    while i < length:
        count_str = ''
        while i < length and compressed_str[i].isdigit():
            count_str += compressed_str[i]
            i += 1
        if i < length:
            char = compressed_str[i]
            i += 1
            decompressed.append(char * int(count_str))
    decompressed_str = ''.join(decompressed)
    integrity_verified = input_string == decompressed_str
    return {'original': input_string, 'compressed': compressed_str, 'decompressed': decompressed_str, 'integrity_verified': integrity_verified}
if __name__ == '__main__':
    sample_input = 'AAAABBBCCDAA'
    result = bidirectional_rle(sample_input)
    print(result)