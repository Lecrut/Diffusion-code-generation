def run_length_encode(text):
    if not text:
        return {}
    result = {}
    current_char = text[0]
    count = 1
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            if current_char in result:
                result[current_char] += count
            else:
                result[current_char] = count
            current_char = char
            count = 1
    if current_char in result:
        result[current_char] += count
    else:
        result[current_char] = count
    return result

if __name__ == '__main__':
    sample_string = "aaabbbaaccccc"
    encoded_result = run_length_encode(sample_string)
    print(encoded_result)
    sample_string_two = "aabbccaaabbb"
    encoded_result_two = run_length_encode(sample_string_two)
    print(encoded_result_two)