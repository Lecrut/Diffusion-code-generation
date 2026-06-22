def encode(data):
    if not data:
        return ""
    encoded = []
    current_char = data[0]
    count = 1
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            encoded.append(f"{count}{current_char}")
            current_char = data[i]
            count = 1
    encoded.append(f"{count}{current_char}")
    return "".join(encoded)

def decode(data):
    if not data:
        return ""
    decoded = []
    i = 0
    while i < len(data):
        num_str = ""
        while i < len(data) and data[i].isdigit():
            num_str += data[i]
            i += 1
        if i >= len(data):
            break
        char = data[i]
        count = int(num_str)
        decoded.append(char * count)
        i += 1
    return "".join(decoded)

if __name__ == '__main__':
    original = "AAABBBCCCCDDDD"
    encoded_result = encode(original)
    decoded_result = decode(encoded_result)
    print(f"Original: {original}")
    print(f"Encoded: {encoded_result}")
    print(f"Decoded: {decoded_result}")
    test_string = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    encoded_test = encode(test_string)
    decoded_test = decode(encoded_test)
    print(f"Test Original: {test_string}")
    print(f"Test Encoded: {encoded_test}")
    print(f"Test Decoded: {decoded_test}")