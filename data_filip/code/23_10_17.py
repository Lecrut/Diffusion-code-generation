def run_length_encode(text):
    if not text:
        return []

    result = []
    current_char = text[0]
    count = 1

    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = text[i]
            count = 1

    result.append((current_char, count))
    return result

if __name__ == '__main__':
    sample1 = "AAABBBCCD"
    sample2 = ""
    sample3 = "A"
    sample4 = "ABCDEF"
    sample5 = "AABBCCDD"
    sample6 = "1122334455"
    sample7 = "   "

    print(run_length_encode(sample1))
    print(run_length_encode(sample2))
    print(run_length_encode(sample3))
    print(run_length_encode(sample4))
    print(run_length_encode(sample5))
    print(run_length_encode(sample6))
    print(run_length_encode(sample7))