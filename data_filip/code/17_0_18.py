def encode_rle(input_string: str) -> str:
    if not input_string:
        return ''
    if len(input_string) < 2:
        return input_string + '1'
    result = []
    count = 1
    current_char = input_string[0]
    for i in range(1, len(input_string)):
        char = input_string[i]
        if char == current_char:
            count += 1
        else:
            result.append(f'{current_char}{count}')
            current_char = char
            count = 1
    result.append(f'{current_char}{count}')
    return ''.join(result)
if __name__ == '__main__':
    sample_input = 'aaabbcccddddd'
    encoded_result = encode_rle(sample_input)
    print(encoded_result)