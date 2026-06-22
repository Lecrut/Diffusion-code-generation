def encode_rle(data: str) -> str:
    if not data:
        return ""
    result = []
    current_char = data[0]
    count = 1
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = data[i]
            count = 1
    result.append(f"{count}{current_char}")
    return "".join(result)

def decode_rle(data: str) -> str:
    if not data:
        return ""
    result = []
    count_str = ""
    for char in data:
        if char.isdigit():
            count_str += char
        else:
            if count_str:
                count = int(count_str)
                result.append(char * count)
                count_str = ""
            else:
                result.append(char)
    return "".join(result)

if __name__ == '__main__':
    sample_input = "AAABBBCCCCCCCCCCDDDDDDDDDDDDEEEE"
    encoded = encode_rle(sample_input)
    decoded = decode_rle(encoded)
    print(encoded)
    print(decoded)