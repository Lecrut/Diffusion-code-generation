def run_length_encode(data):
    if not data:
        return []

    result = []
    count = 1
    char = data[0]
    ordinal = ord(char)

    for i in range(1, len(data)):
        current_char = data[i]
        current_ordinal = ord(current_char)

        if current_char == char:
            count += 1
            if count == 255:
                result.append((255, ordinal))
                count = 0
        else:
            if count > 0:
                result.append((count, ordinal))
            char = current_char
            ordinal = current_ordinal
            count = 1

    if count > 0:
        result.append((count, ordinal))

    return result

if __name__ == '__main__':
    sample_string = "AAABBCDDEE"
    encoded_data = run_length_encode(sample_string)
    print(encoded_data)