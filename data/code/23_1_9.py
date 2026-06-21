def run_length_encode(input_string):
    if not input_string:
        return []
    encoded = []
    current_char = input_string[0]
    count = 1
    for char in input_string[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append((current_char, count))
            current_char = char
            count = 1
    encoded.append((current_char, count))
    return encoded

def run_length_decode(encoded_list):
    if not encoded_list:
        return ""
    return ''.join(char * count for char, count in encoded_list)

if __name__ == '__main__':
    sample_string = "AAABBBCCCDD"
    encoded_result = run_length_encode(sample_string)
    print(encoded_result)
    decoded_result = run_length_decode(encoded_result)
    print(decoded_result)