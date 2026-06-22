def encode_run_length(data):
    if not data:
        return ''
    result = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(f'{count}{current_char}')
            current_char = char
            count = 1
    result.append(f'{count}{current_char}')
    return ''.join(result)

def decode_run_length(data):
    if not data:
        return ''
    result = []
    i = 0
    while i < len(data):
        num_start = i
        while i < len(data) and data[i].isdigit():
            i += 1
        if num_start == i:
            raise ValueError('Invalid run-length encoding: missing count')
        count = int(data[num_start:i])
        if i >= len(data):
            raise ValueError('Invalid run-length encoding: missing character')
        char = data[i]
        i += 1
        result.append(char * count)
    return ''.join(result)

if __name__ == '__main__':
    sample_string = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'
    encoded = encode_run_length(sample_string)
    decoded = decode_run_length(encoded)
    print(encoded)
    print(decoded)
    print('Match:', sample_string == decoded)