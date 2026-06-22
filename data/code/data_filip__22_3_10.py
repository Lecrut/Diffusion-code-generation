def run_length_encode(data):
    if not data:
        return ""
    encoded = []
    count = 1
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            encoded.append(str(count) + data[i - 1])
            count = 1
    encoded.append(str(count) + data[-1])
    return "".join(encoded)

def run_length_decode(data):
    decoded = []
    i = 0
    while i < len(data):
        count = ""
        while i < len(data) and data[i].isdigit():
            count += data[i]
            i += 1
        if i < len(data):
            decoded.append(data[i] * int(count))
            i += 1
    return "".join(decoded)

if __name__ == "__main__":
    sample_string = "WWWWWWWWWWWWBWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    encoded_result = run_length_encode(sample_string)
    decoded_result = run_length_decode(encoded_result)
    print(encoded_result)
    print(decoded_result)