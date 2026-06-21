def run_length_encode(data):
    if not data:
        return ""
    encoded = []
    current_char = data[0]
    count = 1
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
        count_str = ""
        while i < len(data) and data[i].isdigit():
            count_str += data[i]
            i += 1
        if i < len(data):
            char = data[i]
            i += 1
            decoded.append(char * int(count_str))
    return "".join(decoded)

if __name__ == '__main__':
    sample_input = "AAABBBCCCCDD"
    encoded_value = run_length_encode(sample_input)
    decoded_value = run_length_decode(encoded_value)
    print(sample_input == decoded_value)