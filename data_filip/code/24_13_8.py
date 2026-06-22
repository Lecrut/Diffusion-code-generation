def encode(data):
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

def decode(encoded_data):
    if not encoded_data:
        return ""
    result = []
    i = 0
    while i < len(encoded_data):
        j = i
        while j < len(encoded_data) and encoded_data[j].isdigit():
            j += 1
        count = int(encoded_data[i:j])
        char = encoded_data[j]
        result.append(char * count)
        i = j + 1
    return "".join(result)

if __name__ == '__main__':
    sample_input = "AAABBBCCCCDDDDDDD"
    encoded_result = encode(sample_input)
    print(encoded_result)
    decoded_result = decode(encoded_result)
    print(decoded_result)