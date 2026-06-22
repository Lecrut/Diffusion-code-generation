def run_length_encode(data: str) -> str:
    if not data:
        return ''
    encoded_chars = []
    current_char = data[0]
    count = 1
    length = len(data)
    for i in range(1, length):
        char = data[i]
        if char == current_char:
            count += 1
        else:
            encoded_chars.append(str(count) + current_char)
            current_char = char
            count = 1
    encoded_chars.append(str(count) + current_char)
    return ''.join(encoded_chars)

def run_length_decode(data: str) -> str:
    if not data:
        return ''
    decoded_chars = []
    length = len(data)
    i = 0
    while i < length:
        count_str_start = i
        while i < length and data[i].isdigit():
            i += 1
        if i == count_str_start:
            decoded_chars.append(data[i])
            i += 1
            continue
        count = int(data[count_str_start:i])
        if i < length:
            char = data[i]
            decoded_chars.append(char * count)
            i += 1
    return ''.join(decoded_chars)
if __name__ == '__main__':
    original = 'AAAABBBCCDAA'
    encoded = run_length_encode(original)
    decoded = run_length_decode(encoded)
    print(f'Encoded: {encoded}')
    print(f'Decoded: {decoded}')