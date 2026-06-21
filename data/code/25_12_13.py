def encode(data):
    if not data:
        return ""
    encoded = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append(str(count) + current_char)
            current_char = char
            count = 1
    encoded.append(str(count) + current_char)
    return "".join(encoded)

def decode(data):
    if not data:
        return ""
    decoded = []
    i = 0
    while i < len(data):
        if not data[i].isdigit():
            raise ValueError("Invalid encoded data")
        j = i
        while j < len(data) and data[j].isdigit():
            j += 1
        count = int(data[i:j])
        char = data[j]
        decoded.append(char * count)
        i = j + 1
    return "".join(decoded)

if __name__ == '__main__':
    sample_input = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    encoded_result = encode(sample_input)
    decoded_result = decode(encoded_result)
    print(encoded_result)
    print(decoded_result)
    print("Match:", sample_input == decoded_result)