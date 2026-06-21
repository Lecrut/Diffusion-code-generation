def rle_encode(input_string: str) -> str:
    if not input_string:
        return ''
    encoded_chars = []
    prev_char = input_string[0]
    count = 1
    string_length = len(input_string)
    for i in range(1, string_length):
        current_char = input_string[i]
        if current_char == prev_char:
            count += 1
        else:
            encoded_chars.append(str(count))
            encoded_chars.append(prev_char)
            prev_char = current_char
            count = 1
    encoded_chars.append(str(count))
    encoded_chars.append(prev_char)
    return ''.join(encoded_chars)

def rle_decode(input_string: str) -> str:
    if not input_string:
        return ''
    decoded_chars = []
    current_number = []
    string_length = len(input_string)
    for i in range(string_length):
        char = input_string[i]
        if char.isdigit():
            current_number.append(char)
        else:
            count = int(''.join(current_number))
            current_number = []
            decoded_chars.append(char * count)
    return ''.join(decoded_chars)
if __name__ == '__main__':
    original_text = 'AAABBBCCD'
    encoded_text = rle_encode(original_text)
    decoded_text = rle_decode(encoded_text)
    print(encoded_text)
    print(decoded_text)