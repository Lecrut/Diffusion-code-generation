def run_length_encoding(data):
    if not data:
        return ""
    encoded = []
    count = 1
    n = len(data)
    for i in range(1, n):
        if data[i] == data[i - 1]:
            count += 1
        else:
            encoded.append(str(count))
            encoded.append(data[i - 1])
            count = 1
    encoded.append(str(count))
    encoded.append(data[n - 1])
    return "".join(encoded)

if __name__ == '__main__':
    sample_input = "AAABBBCCCCCDDDD"
    result = run_length_encoding(sample_input)
    print(result)
    empty_input = ""
    empty_result = run_length_encoding(empty_input)
    print(empty_result)
    single_char = "Z"
    single_result = run_length_encoding(single_char)
    print(single_result)
    mixed_input = "AABBBCCCCDDDEEFFFF"
    mixed_result = run_length_encoding(mixed_input)
    print(mixed_result)