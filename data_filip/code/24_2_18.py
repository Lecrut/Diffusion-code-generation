def rle_encode(data: str) -> str:
    if not data:
        return ""
    result = []
    count = 1
    current_char = data[0]
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = data[i]
            count = 1
    result.append(f"{count}{current_char}")
    return "".join(result)

def rle_decode(data: str) -> str:
    if not data:
        return ""
    result = []
    count_str = []
    for char in data:
        if char.isdigit():
            count_str.append(char)
        else:
            count = int("".join(count_str))
            result.append(char * count)
            count_str = []
    return "".join(result)

if __name__ == '__main__':
    original = "AAABBBCCDAA"
    encoded = rle_encode(original)
    decoded = rle_decode(encoded)
    print(encoded)
    print(decoded)
    print(original == decoded)