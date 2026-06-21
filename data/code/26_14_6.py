def run_length_encode(input_string):
    if not input_string:
        return ""
    encoded = []
    current_char = input_string[0]
    count = 1
    for i in range(1, len(input_string)):
        if input_string[i] == current_char:
            count += 1
        else:
            encoded.append(current_char + str(count))
            current_char = input_string[i]
            count = 1
    encoded.append(current_char + str(count))
    return "".join(encoded)

if __name__ == '__main__':
    sample_input = "aaabbbccccd"
    result = run_length_encode(sample_input)
    print(result)