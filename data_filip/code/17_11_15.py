def run_length_encode(text: str) -> str:
    if not text:
        return ""

    encoded = []
    count = 1
    current_char = text[0]

    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            encoded.append(current_char + str(count))
            current_char = text[i]
            count = 1

    encoded.append(current_char + str(count))
    return "".join(encoded)

if __name__ == '__main__':
    sample1 = "aaabbbcc"
    sample2 = "abc"
    sample3 = "aabb"
    sample4 = "aaaaa"
    sample5 = ""

    print(run_length_encode(sample1))
    print(run_length_encode(sample2))
    print(run_length_encode(sample3))
    print(run_length_encode(sample4))
    print(run_length_encode(sample5))