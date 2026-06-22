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
    print(run_length_encode("aabcccccaaa"))
    print(run_length_encode("ABC"))
    print(run_length_encode("AABB"))
    print(run_length_encode(""))
    print(run_length_encode("A"))