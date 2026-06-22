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
    sample_string = "AAABBBBCDD"
    result = run_length_encode(sample_string)
    print(result)
    empty_string = ""
    empty_result = run_length_encode(empty_string)
    print(empty_result)
    single_char = "Z"
    single_result = run_length_encode(single_char)
    print(single_result)