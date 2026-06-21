def run_length_encode(data):
    if not data:
        return ""

    encoded_chars = []
    count = 1
    length = len(data)

    for i in range(1, length):
        if data[i] == data[i - 1]:
            count += 1
        else:
            encoded_chars.append(str(count))
            encoded_chars.append(data[i - 1])
            count = 1

    encoded_chars.append(str(count))
    encoded_chars.append(data[-1])

    return "".join(encoded_chars)

if __name__ == '__main__':
    sample_string = "AAABBCDD"
    result = run_length_encode(sample_string)
    print(result)