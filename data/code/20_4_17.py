def run_length_encode(data):
    if not data:
        return ""
    result = []
    count = 1
    length = len(data)
    for i in range(1, length):
        if data[i] == data[i - 1]:
            count += 1
        else:
            result.append(f"{data[i - 1]}{count}")
            count = 1
    result.append(f"{data[-1]}{count}")
    return "".join(result)

if __name__ == '__main__':
    sample_string = "AAAABBBCCDAAA"
    encoded_value = run_length_encode(sample_string)
    print(encoded_value)