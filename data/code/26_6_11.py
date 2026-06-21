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
            encoded.append("{}{}".format(count, current_char))
            current_char = char
            count = 1
    encoded.append("{}{}".format(count, current_char))
    return "".join(encoded)

if __name__ == "__main__":
    sample = "AAABBBCCD"
    result = run_length_encode(sample)
    print(result)