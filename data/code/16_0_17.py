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
            encoded.append(f"{count}{current_char}")
            current_char = data[i]
            count = 1
    encoded.append(f"{count}{current_char}")
    return "".join(encoded)

if __name__ == '__main__':
    test_string = "aaabbbccccdddd"
    result = run_length_encode(test_string)
    print(result)
    test_string_2 = "a1b2c3"
    result_2 = run_length_encode(test_string_2)
    print(result_2)
    empty_string = ""
    result_3 = run_length_encode(empty_string)
    print(result_3)