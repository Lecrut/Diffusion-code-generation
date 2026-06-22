def run_length_encode(data):
    if not data:
        return ""
    encoded = []
    count = 1
    length = len(data)
    for i in range(1, length):
        if data[i] == data[i - 1]:
            count += 1
        else:
            encoded.append(f"{count}{data[i - 1]}")
            count = 1
    encoded.append(f"{count}{data[length - 1]}")
    return "".join(encoded)

if __name__ == '__main__':
    sample_string = "AAABBBCCDA"
    result = run_length_encode(sample_string)
    print(result)