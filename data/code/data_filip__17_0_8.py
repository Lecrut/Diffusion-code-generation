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
            encoded.append(f"{current_char}{count}")
            current_char = text[i]
            count = 1

    encoded.append(f"{current_char}{count}")
    return "".join(encoded)

if __name__ == "__main__":
    sample1 = "AAABBBCCD"
    sample2 = "ABC"
    sample3 = ""
    sample4 = "A"
    sample5 = "AAAABBBCCDAA"

    print(run_length_encode(sample1))
    print(run_length_encode(sample2))
    print(run_length_encode(sample3))
    print(run_length_encode(sample4))
    print(run_length_encode(sample5))