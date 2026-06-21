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
            encoded.append((current_char, count))
            current_char = char
            count = 1
    encoded.append((current_char, count))
    return encoded

def run_length_decode(encoded):
    if not encoded:
        return ""
    decoded = []
    for char, count in encoded:
        decoded.append(char * count)
    return "".join(decoded)

def verify_rle(input_string):
    encoded = run_length_encode(input_string)
    decoded = run_length_decode(encoded)
    return decoded == input_string

if __name__ == '__main__':
    sample_string = "AAABBBCCCCDDEEEEEFFF"
    result = verify_rle(sample_string)
    print(result)