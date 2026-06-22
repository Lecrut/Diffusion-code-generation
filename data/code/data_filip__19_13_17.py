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

if __name__ == '__main__':
    sample_sequence = "aaabbbccccdd"
    result = run_length_encode(sample_sequence)
    print(result)