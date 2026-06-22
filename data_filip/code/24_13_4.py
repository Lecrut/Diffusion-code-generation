def encode(data):
    if not data:
        return ""
    result = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(str(count))
            result.append(current_char)
            current_char = char
            count = 1
    result.append(str(count))
    result.append(current_char)
    return "".join(result)

def decode(data):
    if not data:
        return ""
    result = []
    i = 0
    length = len(data)
    while i < length:
        num_str = []
        while i < length and data[i].isdigit():
            num_str.append(data[i])
            i += 1
        if not num_str:
            break
        count = int("".join(num_str))
        if i < length:
            result.append(data[i] * count)
            i += 1
    return "".join(result)

if __name__ == '__main__':
    sample_input = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
    encoded_value = encode(sample_input)
    print(encoded_value)
    decoded_value = decode(encoded_value)
    print(decoded_value)