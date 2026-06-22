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
            encoded.append(str(count) + current_char)
            current_char = char
            count = 1
    encoded.append(str(count) + current_char)
    return "".join(encoded)

def run_length_decode(encoded):
    if not encoded:
        return ""
    decoded = []
    i = 0
    while i < len(encoded):
        num_str = ""
        while i < len(encoded) and encoded[i].isdigit():
            num_str += encoded[i]
            i += 1
        if i < len(encoded):
            count = int(num_str)
            char = encoded[i]
            decoded.append(char * count)
            i += 1
    return "".join(decoded)

if __name__ == '__main__':
    sample_string = "AAABBBCCCDAA"
    encoded = run_length_encode(sample_string)
    decoded = run_length_decode(encoded)
    print(decoded == sample_string)