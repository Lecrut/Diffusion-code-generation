def encode_run_length(data):
    if not data:
        return ""
    
    result = []
    count = 1
    
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            result.append(str(count) + data[i - 1])
            count = 1
    
    result.append(str(count) + data[-1])
    return "".join(result)

if __name__ == '__main__':
    sample_string = "AAAABBBCCDAAA"
    encoded_value = encode_run_length(sample_string)
    print(encoded_value)
    sample_string_two = "AABBCCC"
    encoded_value_two = encode_run_length(sample_string_two)
    print(encoded_value_two)
    sample_string_three = ""
    encoded_value_three = encode_run_length(sample_string_three)
    print(encoded_value_three)
    sample_string_four = "a1b2c3"
    encoded_value_four = encode_run_length(sample_string_four)
    print(encoded_value_four)