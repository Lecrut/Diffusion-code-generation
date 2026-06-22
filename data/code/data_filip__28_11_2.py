def compress_binary_string(data: str) -> str:
    if not data:
        return ""
    if len(data) == 1:
        return f"{data[0]}1"
    encoded = []
    current_char = data[0]
    count = 1
    index = 1
    total = len(data)
    while index < total:
        char = data[index]
        if char == current_char:
            count += 1
        else:
            encoded.append(f"{current_char}{count}")
            current_char = char
            count = 1
        index += 1
    encoded.append(f"{current_char}{count}")
    return "".join(encoded)

if __name__ == '__main__':
    print(compress_binary_string("0000111010"))
    print(compress_binary_string(""))
    print(compress_binary_string("1"))
    print(compress_binary_string("0000"))
    print(compress_binary_string("11110000"))