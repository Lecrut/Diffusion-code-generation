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
            result.append(str(count))
            result.append(current_char)
            current_char = data[i]
            count = 1
    result.append(str(count))
    result.append(current_char)
    return "".join(result)

def decode(data):
    if not data:
        return ""
    result = []
    i = 0
    while i < len(data):
        count_str = ""
        while i < len(data) and data[i].isdigit():
            count_str += data[i]
            i += 1
        if i < len(data):
            count = int(count_str)
            char = data[i]
            result.append(char * count)
            i += 1
    return "".join(result)

if __name__ == '__main__':
    sample_input = "AAABBBCCCCDDDD"
    encoded = encode(sample_input)
    decoded = decode(encoded)
    print(encoded)
    print(decoded)