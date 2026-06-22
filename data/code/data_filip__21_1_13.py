def run_length_encode(data):
    if not data:
        return {}
    counts = {}
    current_char = data[0]
    count = 1
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            if current_char in counts:
                counts[current_char] += count
            else:
                counts[current_char] = count
            current_char = data[i]
            count = 1
    if current_char in counts:
        counts[current_char] += count
    else:
        counts[current_char] = count
    return counts

if __name__ == '__main__':
    test_input_1 = "aaabbcccc"
    result_1 = run_length_encode(test_input_1)
    print(result_1)
    test_input_2 = "aabbcc"
    result_2 = run_length_encode(test_input_2)
    print(result_2)
    test_input_3 = "xyz"
    result_3 = run_length_encode(test_input_3)
    print(result_3)
    test_input_4 = ""
    result_4 = run_length_encode(test_input_4)
    print(result_4)