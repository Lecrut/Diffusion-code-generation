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
            if count > 1:
                encoded.append(current_char + str(count))
            else:
                encoded.append(current_char)
            current_char = char
            count = 1

    if count > 1:
        encoded.append(current_char + str(count))
    else:
        encoded.append(current_char)

    return "".join(encoded)

if __name__ == '__main__':
    samples = [
        "AAABBBCCD",
        "A",
        "",
        "ABABAB",
        "AAAA",
        "a3b2c1",
        "Hello World!!",
        "1111223"
    ]
    for sample in samples:
        print(run_length_encode(sample))