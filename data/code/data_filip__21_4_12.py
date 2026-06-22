def run_length_encode(text):
    if not text:
        return {}
    result = {}
    current_char = text[0]
    count = 1
    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            if current_char in result:
                result[current_char] += count
            else:
                result[current_char] = count
            current_char = text[i]
            count = 1
    if current_char in result:
        result[current_char] += count
    else:
        result[current_char] = count
    return result

if __name__ == '__main__':
    sample_input = "AAABBBCCCCDDAA"
    encoded_result = run_length_encode(sample_input)
    print(encoded_result)
    sample_input_2 = "Hello World!!"
    encoded_result_2 = run_length_encode(sample_input_2)
    print(encoded_result_2)