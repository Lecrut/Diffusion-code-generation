def run_length_encode(input_string):
    if not input_string:
        return []
    encoded_data = []
    current_char = input_string[0]
    count = 1
    for index in range(1, len(input_string)):
        if input_string[index] == current_char:
            count += 1
        else:
            encoded_data.append((current_char, count))
            current_char = input_string[index]
            count = 1
    encoded_data.append((current_char, count))
    return encoded_data

if __name__ == '__main__':
    sample = 'AAAABBBCCDAA'
    result = run_length_encode(sample)
    print(result)