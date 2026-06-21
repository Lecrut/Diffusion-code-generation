def run_length_encode(data):
    if not data:
        return ""
    encoded = []
    current_char = data[0]
    current_count = 1
    for i in range(1, len(data)):
        char = data[i]
        if char != current_char:
            encoded.append(current_char)
            encoded.append(str(current_count))
            current_char = char
            current_count = 1
        else:
            current_count += 1
    encoded.append(current_char)
    encoded.append(str(current_count))
    return "".join(encoded)

if __name__ == '__main__':
    sample = "hello"
    print(run_length_encode(sample))