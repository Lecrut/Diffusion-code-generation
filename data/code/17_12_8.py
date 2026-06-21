def run_length_encode(input_string):
    if not input_string:
        return {}
    filtered_chars = [char for char in input_string if char.isalnum()]
    if not filtered_chars:
        return {}
    result = {}
    current_char = filtered_chars[0]
    count = 1
    for i in range(1, len(filtered_chars)):
        if filtered_chars[i] == current_char:
            count += 1
        else:
            result[current_char] = count
            current_char = filtered_chars[i]
            count = 1
    result[current_char] = count
    return result

if __name__ == '__main__':
    sample_text = "aa11bb222ccc1111"
    encoded_result = run_length_encode(sample_text)
    print(encoded_result)