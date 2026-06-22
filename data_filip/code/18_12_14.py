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
            encoded.append(str(count) + current_char)
            current_char = char
            count = 1
    encoded.append(str(count) + current_char)
    return "".join(encoded)

if __name__ == "__main__":
    print(run_length_encode("AAABBBCCD"))
    print(run_length_encode("ABC"))
    print(run_length_encode(""))
    print(run_length_encode("A"))
    print(run_length_encode("AABBCC"))