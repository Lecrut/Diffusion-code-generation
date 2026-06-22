def run_length_encode(s):
    if not s:
        return ""
    result = []
    count = 1
    current_char = s[0]
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = s[i]
            count = 1
    result.append(f"{current_char}{count}")
    return "".join(result)

if __name__ == '__main__':
    sample_input = "a11!22bbCCC@@@55"
    encoded_result = run_length_encode(sample_input)
    print(encoded_result)
    sample_input_2 = "aabbcc"
    encoded_result_2 = run_length_encode(sample_input_2)
    print(encoded_result_2)
    sample_input_3 = "!!@@##$$%^^&&"
    encoded_result_3 = run_length_encode(sample_input_3)
    print(encoded_result_3)