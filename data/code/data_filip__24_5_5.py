def encode(data: str) -> str:
    if not data:
        return ""
    result = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
    result.append(f"{count}{current_char}")
    return "".join(result)

def decode(data: str) -> str:
    if not data:
        return ""
    result = []
    i = 0
    while i < len(data):
        count_str = []
        while i < len(data) and data[i].isdigit():
            count_str.append(data[i])
            i += 1
        if not count_str:
            raise ValueError("Invalid encoding: missing count")
        count = int("".join(count_str))
        if i >= len(data):
            raise ValueError("Invalid encoding: missing character")
        char = data[i]
        result.append(char * count)
        i += 1
    return "".join(result)

if __name__ == '__main__':
    print(encode("aaabbbbcccc"))
    print(decode("3a4b4c"))