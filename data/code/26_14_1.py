def run_length_encode(input_string):
    if not input_string:
        return ""

    result = []
    count = 1
    current_char = input_string[0]

    for i in range(1, len(input_string)):
        char = input_string[i]
        if char == current_char:
            count += 1
        else:
            result.append(current_char + str(count))
            current_char = char
            count = 1

    result.append(current_char + str(count))
    return "".join(result)

if __name__ == '__main__':
    sample_text = "aaabbc"
    encoded_text = run_length_encode(sample_text)
    print(encoded_text)