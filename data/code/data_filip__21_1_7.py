def run_length_encode(data):
    if not data:
        return {}
    result = {}
    current_char = data[0]
    count = 1
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            result[current_char] = count
            current_char = data[i]
            count = 1
    result[current_char] = count
    return result

if __name__ == '__main__':
    test_string = "aaabbcdddd"
    encoded_result = run_length_encode(test_string)
    print(encoded_result)
    test_string_2 = "zzz"
    encoded_result_2 = run_length_encode(test_string_2)
    print(encoded_result_2)
    test_string_3 = ""
    encoded_result_3 = run_length_encode(test_string_3)
    print(encoded_result_3)