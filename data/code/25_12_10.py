def rle_encode(data):
    if not data:
        return ""
    encoded = []
    current_char = data[0]
    count = 1
    for char in data[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append(f"{count}{current_char}")
            current_char = char
            count = 1
    encoded.append(f"{count}{current_char}")
    return "".join(encoded)

def rle_decode(data):
    if not data:
        return ""
    decoded = []
    i = 0
    while i < len(data):
        if not data[i].isdigit():
            break
        j = i
        while j < len(data) and data[j].isdigit():
            j += 1
        count = int(data[i:j])
        if j < len(data):
            decoded.append(data[j] * count)
            i = j + 1
        else:
            break
    return "".join(decoded)

if __name__ == '__main__':
    sample_input = "AAAABBBCCDAABBB"
    encoded_result = rle_encode(sample_input)
    decoded_result = rle_decode(encoded_result)
    print(f"Original: {sample_input}")
    print(f"Encoded: {encoded_result}")
    print(f"Decoded: {decoded_result}")
    
    test_string = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    encoded_test = rle_encode(test_string)
    decoded_test = rle_decode(encoded_test)
    print(f"Original: {test_string}")
    print(f"Encoded: {encoded_test}")
    print(f"Decoded: {decoded_test}")