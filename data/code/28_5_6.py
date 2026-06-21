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
            encoded.append(f"{count}{current_char}")
            current_char = input_string[i]
            count = 1
    encoded.append(f"{count}{current_char}")
    return "".join(encoded)

def run_length_decode(encoded_string):
    if not encoded_string:
        return ""
    decoded = []
    i = 0
    while i < len(encoded_string):
        count_str = ""
        while i < len(encoded_string) and encoded_string[i].isdigit():
            count_str += encoded_string[i]
            i += 1
        if i < len(encoded_string):
            char = encoded_string[i]
            count = int(count_str)
            decoded.append(char * count)
            i += 1
    return "".join(decoded)

if __name__ == '__main__':
    sample_input = "AAABBCDDDDD"
    encoded_result = run_length_encode(sample_input)
    decoded_result = run_length_decode(encoded_result)
    print(sample_input == decoded_result)