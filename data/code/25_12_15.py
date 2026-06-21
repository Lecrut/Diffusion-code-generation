def run_length_encode(data: str) -> list:
    if not data:
        return []
    encoded = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append((current_char, count))
            current_char = char
            count = 1
    encoded.append((current_char, count))
    return encoded

def run_length_decode(encoded: list) -> str:
    decoded = []
    for char, count in encoded:
        decoded.append(char * count)
    return ''.join(decoded)

def bidirectional_rle(data: str, mode: str = 'encode') -> any:
    if mode == 'encode':
        return run_length_encode(data)
    elif mode == 'decode':
        return run_length_decode(data)
    else:
        raise ValueError("Mode must be 'encode' or 'decode'")

if __name__ == '__main__':
    sample_data = 'AAABBBCCDAA'
    encoded = bidirectional_rle(sample_data, 'encode')
    print(encoded)
    decoded = bidirectional_rle(encoded, 'decode')
    print(decoded)