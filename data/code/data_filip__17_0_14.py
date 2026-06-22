def run_length_encode(text):
    if not text:
        return ""

    encoded = []
    current_char = text[0]
    count = 1

    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            encoded.append(current_char)
            encoded.append(str(count))
            current_char = text[i]
            count = 1

    encoded.append(current_char)
    encoded.append(str(count))

    return "".join(encoded)

if __name__ == "__main__":
    sample1 = "AABCCC"
    print(run_length_encode(sample1))

    sample2 = "XYZ"
    print(run_length_encode(sample2))

    sample3 = "PPPPPP"
    print(run_length_encode(sample3))

    sample4 = ""
    print(run_length_encode(sample4))

    sample5 = "a"
    print(run_length_encode(sample5))