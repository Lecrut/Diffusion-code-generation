def decode_rle(encoded_string: str) -> str:
    if not encoded_string:
        return ''
    decoded_chars = []
    i = 0
    length = len(encoded_string)
    while i < length:
        if i >= length:
            break
        char = encoded_string[i]
        i += 1
        count_str = ''
        while i < length and encoded_string[i].isdigit():
            count_str += encoded_string[i]
            i += 1
        count = int(count_str) if count_str else 1
        decoded_chars.extend([char] * count)
    return ''.join(decoded_chars)
if __name__ == '__main__':
    encoded = '3a4b2c1d'
    result = decode_rle(encoded)
    print(result)