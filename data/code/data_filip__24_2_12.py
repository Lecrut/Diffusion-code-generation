def encode_rle(data):
    if not data:
        return ""
    encoded = []
    count = 1
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            encoded.append(f"{count}{data[i - 1]}")
            count = 1
    encoded.append(f"{count}{data[-1]}")
    return "".join(encoded)

def decode_rle(data):
    if not data:
        return ""
    decoded = []
    i = 0
    while i < len(data):
        count_str = ""
        while i < len(data) and data[i].isdigit():
            count_str += data[i]
            i += 1
        if i < len(data):
            char = data[i]
            decoded.append(char * int(count_str))
            i += 1
    return "".join(decoded)

if __name__ == "__main__":
    test_strings = ["AAABBBCCDA", "WWWWWWWWWWWWB", ""]
    for s in test_strings:
        encoded = encode_rle(s)
        decoded = decode_rle(encoded)
        print(f"Original: {s}")
        print(f"Encoded: {encoded}")
        print(f"Decoded: {decoded}")
        print(f"Fidelity: {s == decoded}")
        print("-" * 20)