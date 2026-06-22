def run_length_encoding(data):
    if not data:
        return ""
    result = []
    count = 1
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            result.append(str(count))
            result.append(data[i - 1])
            count = 1
    result.append(str(count))
    result.append(data[-1])
    return "".join(result)

if __name__ == '__main__':
    sample_input = "AAAABBBCCDA"
    print(run_length_encoding(sample_input))