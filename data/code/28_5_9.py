def run_length_encode(text):
    if not text:
        return ""
    encoded = []
    current_char = text[0]
    count = 1
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append(f"{count}{current_char}")
            current_char = char
            count = 1
    encoded.append(f"{count}{current_char}")
    return "".join(encoded)

def run_length_decode(encoded):
    decoded = []
    i = 0
    while i < len(encoded):
        if not encoded[i].isdigit():
            decoded.append(encoded[i])
            i += 1
        else:
            count_str = ""
            while i < len(encoded) and encoded[i].isdigit():
                count_str += encoded[i]
                i += 1
            count = int(count_str)
            if i < len(encoded):
                char = encoded[i]
                decoded.append(char * count)
                i += 1
    return "".join(decoded)

if __name__ == '__main__':
    sample_input = "AAABBBCCD"
    encoded = run_length_encode(sample_input)
    decoded = run_length_decode(encoded)
    print(decoded == sample_input)