def compress_string(data: str) -> str:
    if not data:
        return ""
    result = []
    current_char = data[0]
    count = 1
    for index in range(1, len(data)):
        char = data[index]
        if char == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = char
            count = 1
    result.append(f"{current_char}{count}")
    return "".join(result)

if __name__ == "__main__":
    sample_input = "aaabbccccd"
    compressed_output = compress_string(sample_input)
    print(compressed_output)