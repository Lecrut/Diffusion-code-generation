def encode(data):
    if not data:
        return ""
    result = []
    count = 1
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            result.append(str(count) + data[i - 1])
            count = 1
    result.append(str(count) + data[-1])
    return "".join(result)

def decode(data):
    if not data:
        return ""
    result = []
    i = 0
    while i < len(data):
        num_str = ""
        while i < len(data) and data[i].isdigit():
            num_str += data[i]
            i += 1
        if i < len(data):
            count = int(num_str)
            char = data[i]
            result.append(char * count)
            i += 1
    return "".join(result)

if __name__ == "__main__":
    sample_input = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    encoded = encode(sample_input)
    print(encoded)
    decoded = decode(encoded)
    print(decoded)