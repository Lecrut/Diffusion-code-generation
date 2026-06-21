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
            encoded_result.append(str(count) + current_char)
            current_char = input_string[i]
            count = 1
    encoded_result.append(str(count) + current_char)
    return "".join(encoded_result)

if __name__ == '__main__':
    sample_text = "aaabbccccd"
    encoded_sample = run_length_encode(sample_text)
    print(encoded_sample)
    sample_text_two = "!@@##!!"
    encoded_sample_two = run_length_encode(sample_text_two)
    print(encoded_sample_two)
    sample_text_three = ""
    encoded_sample_three = run_length_encode(sample_text_three)
    print(encoded_sample_three)
    sample_text_four = "a"
    encoded_sample_four = run_length_encode(sample_text_four)
    print(encoded_sample_four)