def run_length_encode(data):
    if not data:
        return ""
    encoded = []
    current_char = data[0]
    count = 1
    for i in range(1, len(data)):
        char = data[i]
        if char == current_char:
            count += 1
        else:
            encoded.append(f"{count}{current_char}")
            current_char = char
            count = 1
    encoded.append(f"{count}{current_char}")
    return "".join(encoded)

def run_length_decode(data):
    if not data:
        return ""
    decoded = []
    i = 0
    while i < len(data):
        count_str = ""
        while i < len(data) and data[i].isdigit():
            count_str += data[i]
            i += 1
        count = int(count_str)
        char = data[i]
        decoded.append(char * count)
        i += 1
    return "".join(decoded)

if __name__ == '__main__':
    original = "AAABBBCCCC"
    compressed = run_length_encode(original)
    decompressed = run_length_decode(compressed)
    print(f"Original: {original}")
    print(f"Compressed: {compressed}")
    print(f"Decompressed: {decompressed}")