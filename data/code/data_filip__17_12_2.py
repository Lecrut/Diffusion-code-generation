def encode_rle(input_string):
    if not input_string:
        return {}

    encoded_dict = {}
    current_char = input_string[0]
    count = 1
    result_list = []

    for i in range(1, len(input_string)):
        char = input_string[i]
        if char.isalnum() and char == current_char:
            count += 1
        else:
            if current_char.isalnum():
                result_list.append((current_char, count))
            current_char = char
            count = 1

    if current_char.isalnum():
        result_list.append((current_char, count))

    for char, freq in result_list:
        encoded_dict[char] = freq

    return encoded_dict

if __name__ == '__main__':
    sample_text = "aabbccccd"
    result = encode_rle(sample_text)
    print(result)