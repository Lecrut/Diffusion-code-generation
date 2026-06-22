def run_length_encode(s):
    if not s:
        return ""
    encoded = []
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append((current_char, count))
            current_char = char
            count = 1
    encoded.append((current_char, count))
    return encoded

def decode_run_length(encoded):
    decoded = []
    for char, count in encoded:
        decoded.append(char * count)
    return "".join(decoded)

if __name__ == '__main__':
    sample_string = "AAABBBCCCDDE"
    encoded_data = run_length_encode(sample_string)
    print(sample_string)
    print(encoded_data)