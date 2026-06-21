def run_length_encode(input_string):
    if not input_string:
        return []

    encoded_list = []
    current_char = input_string[0]
    current_count = 1

    for index in range(1, len(input_string)):
        char = input_string[index]
        if char == current_char:
            current_count += 1
        else:
            encoded_list.append((current_char, current_count))
            current_char = char
            current_count = 1

    encoded_list.append((current_char, current_count))

    return encoded_list

if __name__ == '__main__':
    data = 'AAAABBBCCDAA'
    result = run_length_encode(data)
    print(result)