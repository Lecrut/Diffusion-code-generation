def run_length_encode(data):
    if not data:
        return ""
    encoded = []
    count = 1
    current_char = data[0]
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append(f"{count}{current_char}")
            current_char = char
            count = 1
    encoded.append(f"{count}{current_char}")
    return "".join(encoded)

def run_length_decode(data):
    if not data:
        return ""
    decoded = []
    i = 0
    while i < len(data):
        if not data[i].isdigit():
            return ""
        count_str = ""
        while i < len(data) and data[i].isdigit():
            count_str += data[i]
            i += 1
        if i >= len(data):
            return ""
        char = data[i]
        count = int(count_str)
        decoded.append(char * count)
        i += 1
    return "".join(decoded)

if __name__ == '__main__':
    sample_input = "AAABBCDDDD"
    encoded_data = run_length_encode(sample_input)
    decoded_data = run_length_decode(encoded_data)
    print(sample_input == decoded_data)