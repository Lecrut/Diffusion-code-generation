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
    if not encoded:
        return ""
    decoded_parts = []
    for char, count in encoded:
        decoded_parts.append(char * count)
    return "".join(decoded_parts)

if __name__ == '__main__':
    sample_data = "AAABBBCCDAA"
    encoded = run_length_encode(sample_data)
    decoded = run_length_decode(encoded)
    print(encoded)
    print(decoded)