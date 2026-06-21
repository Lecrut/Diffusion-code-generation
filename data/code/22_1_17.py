def run_length_encoding(input_string):
    if not input_string:
        return []
    result = []
    current_char = input_string[0]
    count = 1
    for char in input_string[1:]:
        if char == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = char
            count = 1
    result.append((current_char, count))
    return result

if __name__ == '__main__':
    test_string = "aaabbbaacccccd"
    encoded_data = run_length_encoding(test_string)
    print(encoded_data)