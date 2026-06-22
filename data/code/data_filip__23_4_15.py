def run_length_encode(text: str) -> str:
    if not text:
        return ""

    result = []
    count = 1
    current_char = text[0]

    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            result.append(str(count))
            result.append(current_char)
            current_char = text[i]
            count = 1

    result.append(str(count))
    result.append(current_char)

    return "".join(result)

def run_length_decode(encoded_text: str) -> str:
    if not encoded_text:
        return ""

    result = []
    count_str = []

    for char in encoded_text:
        if char.isdigit():
            count_str.append(char)
        else:
            count = int("".join(count_str))
            result.append(char * count)
            count_str = []

    return "".join(result)

if __name__ == '__main__':
    sample_text = "AAABBBCCC"
    encoded = run_length_encode(sample_text)
    print(encoded)

    sample_encoded = "3A3B3C"
    decoded = run_length_decode(sample_encoded)
    print(decoded)

    multi_digit_text = "AAAAAAAAAA"
    encoded_multi = run_length_encode(multi_digit_text)
    print(encoded_multi)

    decoded_multi = run_length_decode(encoded_multi)
    print(decoded_multi)