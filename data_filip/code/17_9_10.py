def run_length_encode(data):
    if not data:
        return ""
    encoded = []
    current_char = data[0]
    count = 1
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            encoded.append(current_char)
            encoded.append(str(count))
            current_char = data[i]
            count = 1
    encoded.append(current_char)
    encoded.append(str(count))
    return "".join(encoded)

if __name__ == '__main__':
    sample_input = "AAABBBCCCDDEE"
    result = run_length_encode(sample_input)
    print(result)
    empty_input = ""
    empty_result = run_length_encode(empty_input)
    print(empty_result)
    single_input = "Z"
    single_result = run_length_encode(single_input)
    print(single_result)