def run_length_encode(text):
    if not text:
        return ""
    result = []
    current_char = text[0]
    count = 1
    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = text[i]
            count = 1
    result.append(f"{count}{current_char}")
    return "".join(result)

def run_length_decode(text):
    if not text:
        return ""
    result = []
    i = 0
    while i < len(text):
        num_str = ""
        while i < len(text) and text[i].isdigit():
            num_str += text[i]
            i += 1
        if i < len(text):
            count = int(num_str)
            char = text[i]
            result.append(char * count)
            i += 1
    return "".join(result)

if __name__ == '__main__':
    sample_string = "AAABBBCCCCDDDDDE"
    encoded = run_length_encode(sample_string)
    print(encoded)
    decoded = run_length_decode(encoded)
    print(decoded)
    complex_string = "A12B34C5"
    encoded_complex = run_length_encode(complex_string)
    print(encoded_complex)
    decoded_complex = run_length_decode(encoded_complex)
    print(decoded_complex)