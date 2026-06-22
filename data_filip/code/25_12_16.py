def encode(data):
    if not data:
        return ""
    encoded = []
    count = 1
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            encoded.append(str(count) + data[i - 1])
            count = 1
    encoded.append(str(count) + data[-1])
    return "".join(encoded)

def decode(data):
    if not data:
        return ""
    decoded = []
    i = 0
    while i < len(data):
        j = i
        while j < len(data) and data[j].isdigit():
            j += 1
        if j == i:
            raise ValueError("Invalid encoded data: missing count")
        count = int(data[i:j])
        if j >= len(data):
            raise ValueError("Invalid encoded data: missing character")
        decoded.append(data[j] * count)
        i = j + 1
    return "".join(decoded)

if __name__ == "__main__":
    original = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    encoded_value = encode(original)
    decoded_value = decode(encoded_value)
    print(f"Original: {original}")
    print(f"Encoded: {encoded_value}")
    print(f"Decoded: {decoded_value}")