def run_length_encode(input_string):
    if not input_string:
        return ""
    encoded_result = []
    current_char = input_string[0]
    count = 1
    for i in range(1, len(input_string)):
        if input_string[i] == current_char:
            count += 1
        else:
            encoded_result.append(current_char)
            encoded_result.append(str(count))
            current_char = input_string[i]
            count = 1
    encoded_result.append(current_char)
    encoded_result.append(str(count))
    return "".join(encoded_result)

if __name__ == '__main__':
    sample_data = "aabcccccaaa"
    print(run_length_encode(sample_data))
    sample_data_2 = "A111BB22"
    print(run_length_encode(sample_data_2))