def run_length_encode(data):
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

def run_length_decode(encoded):
    if not encoded:
        return ""
    decoded = []
    i = 0
    while i < len(encoded):
        if not encoded[i].isdigit():
            decoded.append(encoded[i])
            i += 1
        else:
            count_str = ""
            while i < len(encoded) and encoded[i].isdigit():
                count_str += encoded[i]
                i += 1
            count = int(count_str)
            if i < len(encoded):
                decoded.append(encoded[i] * count)
                i += 1
            else:
                decoded.append(' ' * count)
    return "".join(decoded)

def verify_rle(original):
    encoded = run_length_encode(original)
    decoded = run_length_decode(encoded)
    return original == decoded

if __name__ == '__main__':
    sample_input = "AAABBBCCCCD"
    result = verify_rle(sample_input)
    print(result)