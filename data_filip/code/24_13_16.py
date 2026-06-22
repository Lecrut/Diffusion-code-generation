def encode_run_length(data: str) -> str:
    if not data:
        return ""
    result = []
    count = 1
    current_char = data[0]
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

def decode_run_length(encoded_data: str) -> str:
    if not encoded_data:
        return ""
    result = []
    i = 0
    while i < len(encoded_data):
        count_str = []
        while i < len(encoded_data) and encoded_data[i].isdigit():
            count_str.append(encoded_data[i])
            i += 1
        count = int("".join(count_str))
        if i < len(encoded_data):
            char = encoded_data[i]
            i += 1
            result.append(char * count)
    return "".join(result)

if __name__ == '__main__':
    original_text = "AAABBBCCDAA"
    encoded = encode_run_length(original_text)
    print(encoded)
    decoded = decode_run_length(encoded)
    print(decoded)