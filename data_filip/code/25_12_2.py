def run_length_encode(data: str) -> str:
    if not data:
        return ""
    encoded = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append(f"{count}{current_char}")
            current_char = char
            count = 1
    encoded.append(f"{count}{current_char}")
    return "".join(encoded)

def run_length_decode(data: str) -> str:
    if not data:
        return ""
    decoded = []
    i = 0
    length = len(data)
    while i < length:
        num_str = []
        while i < length and data[i].isdigit():
            num_str.append(data[i])
            i += 1
        count = int("".join(num_str))
        if i < length:
            char = data[i]
            i += 1
            decoded.append(char * count)
    return "".join(decoded)

if __name__ == '__main__':
    original_text = "AAAABBBCCDAA"
    encoded_text = run_length_encode(original_text)
    decoded_text = run_length_decode(encoded_text)
    print(f"Original: {original_text}")
    print(f"Encoded:  {encoded_text}")
    print(f"Decoded:  {decoded_text}")