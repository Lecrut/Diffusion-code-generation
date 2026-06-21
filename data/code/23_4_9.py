def run_length_encode(text):
    if not text:
        return ''
    encoded = []
    current_char = text[0]
    count = 1
    for i in range(1, len(text)):
        char = text[i]
        if char == current_char:
            count += 1
        else:
            if count > 9:
                encoded.append(f'{count}{current_char}')
            else:
                encoded.append(f'{count}{current_char}')
            current_char = char
            count = 1
    if count > 9:
        encoded.append(f'{count}{current_char}')
    else:
        encoded.append(f'{count}{current_char}')
    return ''.join(encoded)

def run_length_decode(encoded_text):
    if not encoded_text:
        return ''
    decoded = []
    i = 0
    while i < len(encoded_text):
        count_str = []
        while i < len(encoded_text) and encoded_text[i].isdigit():
            count_str.append(encoded_text[i])
            i += 1
        count = int(''.join(count_str))
        if i < len(encoded_text):
            char = encoded_text[i]
            i += 1
            decoded.append(char * count)
        else:
            break
    return ''.join(decoded)
if __name__ == '__main__':
    original = 'AAAABBBCCDAA'
    encoded = run_length_encode(original)
    print(encoded)
    decoded = run_length_decode(encoded)
    print(decoded)
    original_multi = 'AAAAABBBBBCCCCCC'
    encoded_multi = run_length_encode(original_multi)
    print(encoded_multi)
    decoded_multi = run_length_decode(encoded_multi)
    print(decoded_multi)