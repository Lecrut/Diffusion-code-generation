def run_length_encode(data):
    if not data:
        return ""
    encoded = []
    count = 1
    current_char = data[0]
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            encoded.append(str(count) + current_char)
            current_char = data[i]
            count = 1
    encoded.append(str(count) + current_char)
    return "".join(encoded)

if __name__ == '__main__':
    original_string = "AAAABBBCCDAA"
    compressed_string = run_length_encode(original_string)
    print("Original:", original_string)
    print("Compressed:", compressed_string)