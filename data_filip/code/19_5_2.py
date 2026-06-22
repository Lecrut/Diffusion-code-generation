def rle_constrained_encode(data, max_run_length):
    if not data:
        return ''
    if max_run_length < 1:
        raise ValueError('max_run_length must be at least 1')
    result = []
    run_count = 0
    current_char = data[0]
    for char in data:
        if char == current_char and run_count < max_run_length:
            run_count += 1
        else:
            result.append(f'{run_count}{current_char}')
            current_char = char
            run_count = 1
    result.append(f'{run_count}{current_char}')
    return ''.join(result)

def rle_constrained_decode(encoded_str):
    if not encoded_str:
        return ''
    result = []
    i = 0
    length = len(encoded_str)
    while i < length:
        count_str_start = i
        while i < length and encoded_str[i].isdigit():
            i += 1
        if count_str_start == i:
            raise ValueError('Invalid encoded string: expected digits')
        count = int(encoded_str[count_str_start:i])
        if i < length:
            char = encoded_str[i]
            i += 1
            result.append(char * count)
        else:
            raise ValueError('Invalid encoded string: missing character after count')
    return ''.join(result)
if __name__ == '__main__':
    original_text = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBB'
    max_run = 5
    encoded = rle_constrained_encode(original_text, max_run)
    decoded = rle_constrained_decode(encoded)
    print(encoded)
    print(decoded)
    print(original_text == decoded)