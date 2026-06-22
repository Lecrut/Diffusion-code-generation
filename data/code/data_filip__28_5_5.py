def run_length_encode(text):
    if not text:
        return ""
    encoded = []
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            encoded.append(f"{count}{text[i - 1]}")
            count = 1
    encoded.append(f"{count}{text[-1]}")
    return "".join(encoded)

def run_length_decode(encoded_text):
    if not encoded_text:
        return ""
    decoded = []
    i = 0
    while i < len(encoded_text):
        j = i
        while j < len(encoded_text) and encoded_text[j].isdigit():
            j += 1
        if j == i:
            break
        count = int(encoded_text[i:j])
        char = encoded_text[j]
        decoded.append(char * count)
        i = j + 1
    return "".join(decoded)

if __name__ == '__main__':
    sample_input = "AAABBCDDDDD"
    encoded_result = run_length_encode(sample_input)
    decoded_result = run_length_decode(encoded_result)
    print(sample_input == decoded_result)