def encode_rle(data: str) -> str:
    if not data:
        return ""
    result = []
    current_char = data[0]
    count = 1
    for i in range(1, len(data)):
        char = data[i]
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
    result.append(f"{count}{current_char}")
    return "".join(result)

def decode_rle(data: str) -> str:
    if not data:
        return ""
    result = []
    i = 0
    while i < len(data):
        count_str = ""
        while i < len(data) and data[i].isdigit():
            count_str += data[i]
            i += 1
        if i < len(data):
            char = data[i]
            i += 1
            if count_str:
                count = int(count_str)
                result.append(char * count)
            else:
                result.append(char)
    return "".join(result)

if __name__ == '__main__':
    sample_data = "0011100"
    encoded = encode_rle(sample_data)
    print(encoded)
    decoded = decode_rle(encoded)
    print(decoded)