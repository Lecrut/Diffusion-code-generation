def run_length_encode(input_string):
    if not input_string:
        return []
    result = []
    current_char = input_string[0]
    count = 1
    for i in range(1, len(input_string)):
        if input_string[i] == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = input_string[i]
            count = 1
    result.append((current_char, count))
    return result

if __name__ == '__main__':
    sample_input_1 = "aaabbc"
    sample_input_2 = ""
    sample_input_3 = "a"
    sample_input_4 = "111222333"
    print(run_length_encode(sample_input_1))
    print(run_length_encode(sample_input_2))
    print(run_length_encode(sample_input_3))
    print(run_length_encode(sample_input_4))