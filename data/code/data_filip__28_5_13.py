def run_length_encode(data):
    if not data:
        return ""
    encoded = ""
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            encoded += str(count) + current_char
            current_char = char
            count = 1
    encoded += str(count) + current_char
    return encoded

def run_length_decode(encoded):
    decoded = ""
    i = 0
    while i < len(encoded):
        count = ""
        while i < len(encoded) and encoded[i].isdigit():
            count += encoded[i]
            i += 1
        char = encoded[i]
        i += 1
        decoded += char * int(count)
    return decoded

if __name__ == '__main__':
    sample_input = "AAABBBCCDAA"
    encoded = run_length_encode(sample_input)
    decoded = run_length_decode(encoded)
    print(decoded == sample_input)