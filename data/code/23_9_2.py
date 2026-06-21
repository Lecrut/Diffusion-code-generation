def run_length_encode(input_string):
    if not input_string:
        return ""

    encoded = []
    length = len(input_string)
    index = 0

    while index < length:
        current_char = input_string[index]
        count = 1
        while index + 1 < length and input_string[index + 1] == current_char:
            index += 1
            count += 1
        encoded.append(current_char)
        encoded.append(str(count))
        index += 1

    return "".join(encoded)

if __name__ == '__main__':
    sample = "aaabbbcc"
    result = run_length_encode(sample)
    print(result)