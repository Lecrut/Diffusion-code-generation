def encode(data):
    if not data:
        return ""
    result = []
    count = 1
    current_char = data[0]
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            result.append(str(count))
            result.append(current_char)
            current_char = data[i]
            count = 1
    result.append(str(count))
    result.append(current_char)
    return "".join(result)

def decode(data):
    if not data:
        return ""
    result = []
    count_str = ""
    for char in data:
        if char.isdigit():
            count_str += char
        else:
            count = int(count_str)
            result.append(char * count)
            count_str = ""
    return "".join(result)

if __name__ == '__main__':
    sample_input = "WWWWWWWWWWWWBWWWWWWWWWWWWBBB"
    encoded_value = encode(sample_input)
    decoded_value = decode(encoded_value)
    print(encoded_value)
    print(decoded_value)
    multi_digit_test = "AAAAAAAAAAABBBBBBBBBBBBCCCCCCCCCC"
    print(encode(multi_digit_test))
    print(decode(encode(multi_digit_test)))