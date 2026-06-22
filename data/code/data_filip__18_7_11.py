def run_length_encode(data: str) -> str:
    if not data:
        return ""

    result = []
    current_char = data[0]
    count = 1
    length = len(data)

    for i in range(1, length):
        char = data[i]
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1

    result.append(f"{count}{current_char}")

    return "".join(result)

def run_length_decode(data: str) -> str:
    if not data:
        return ""

    result = []
    length = len(data)
    i = 0

    while i < length:
        count_str = []
        while i < length and data[i].isdigit():
            count_str.append(data[i])
            i += 1
        count = int("".join(count_str))
        char = data[i]
        i += 1
        result.append(char * count)

    return "".join(result)

if __name__ == '__main__':
    original_string = "AABBBCCCCDDDDEEEE"
    encoded = run_length_encode(original_string)
    print(encoded)
    decoded = run_length_decode(encoded)
    print(decoded)
    print(original_string == decoded)