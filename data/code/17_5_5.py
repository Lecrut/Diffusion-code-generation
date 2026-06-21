def run_length_encode(input_string):
    if not input_string:
        return ""
    result = []
    count = 1
    length = len(input_string)
    for i in range(length):
        if i + 1 < length and input_string[i] == input_string[i + 1]:
            count += 1
        else:
            result.append(f"{count}{input_string[i]}")
            count = 1
    return "".join(result)

if __name__ == '__main__':
    sample_input = "AAAABBBCCDAABBB"
    encoded_result = run_length_encode(sample_input)
    print(encoded_result)