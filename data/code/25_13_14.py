def _get_groups(data):
    groups = []
    if not data:
        return groups
    current_char = data[0]
    count = 1
    data_len = len(data)
    idx = 1
    while idx < data_len:
        char = data[idx]
        if char == current_char:
            count += 1
        else:
            groups.append((current_char, count))
            current_char = char
            count = 1
        idx += 1
    groups.append((current_char, count))
    return groups

def run_length_encode(data: str) -> str:
    groups = _get_groups(data)
    parts = []
    for char, count in groups:
        if count > 9:
            digits = []
            temp = count
            while temp > 0:
                digits.append(str(temp % 10))
                temp //= 10
            digits.reverse()
            parts.append("".join(digits))
        else:
            parts.append(str(count))
        parts.append(char)
    return "".join(parts)

def run_length_decode(encoded: str) -> str:
    if not encoded:
        return ""
    decoded = []
    buffer = 0
    has_number = False
    data_len = len(encoded)
    idx = 0
    while idx < data_len:
        char = encoded[idx]
        if char.isdigit():
            buffer = buffer * 10 + int(char)
            has_number = True
        else:
            if has_number:
                count = buffer
                decoded.append(char * count)
                buffer = 0
                has_number = False
            else:
                decoded.append(char)
        idx += 1
    if has_number:
        decoded.append(encoded[-1] * buffer)
    return "".join(decoded)

if __name__ == '__main__':
    original = "AAABBC"
    encoded = run_length_encode(original)
    decoded = run_length_decode(encoded)
    print(f"Encoded: {encoded}")
    print(f"Decoded: {decoded}")
    print(f"Match: {original == decoded}")
    
    original2 = "aabbccc"
    encoded2 = run_length_encode(original2)
    print(f"Encoded2: {encoded2}")
    print(f"Match2: {original2 == run_length_decode(encoded2)}")