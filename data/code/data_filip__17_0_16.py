def run_length_encode(input_string):
    if not input_string:
        return ""

    encoded_chars = []
    count = 1
    length = len(input_string)

    for i in range(1, length):
        if input_string[i] == input_string[i - 1]:
            count += 1
        else:
            encoded_chars.append(input_string[i - 1])
            encoded_chars.append(str(count))
            count = 1

    encoded_chars.append(input_string[length - 1])
    encoded_chars.append(str(count))

    return "".join(encoded_chars)

if __name__ == '__main__':
    result = run_length_encode("AAAABBBCCDAA")
    print(result)