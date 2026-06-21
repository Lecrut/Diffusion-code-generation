def run_length_encode(text):
    if not text:
        return ""
    result = []
    count = 1
    length = len(text)
    for i in range(length):
        if i + 1 < length and text[i] == text[i + 1]:
            count += 1
        else:
            result.append(str(count))
            result.append(text[i])
            count = 1
    return "".join(result)

if __name__ == '__main__':
    sample_string = "aaabbcdddd"
    encoded_result = run_length_encode(sample_string)
    print(encoded_result)
    sample_string_2 = "a"
    encoded_result_2 = run_length_encode(sample_string_2)
    print(encoded_result_2)
    sample_string_3 = ""
    encoded_result_3 = run_length_encode(sample_string_3)
    print(encoded_result_3)