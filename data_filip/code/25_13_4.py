def run_length_encode(data: str) -> list:
    if not data:
        return []
    encoded = []
    count = 1
    current_char = data[0]
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

if __name__ == '__main__':
    sample_data = "AAAABBBCCDAA"
    encoded = run_length_encode(sample_data)
    print(encoded)
    decoded = run_length_decode(encoded)
    print(decoded)
    assert decoded == sample_data