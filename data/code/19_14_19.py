def run_length_encode(text):
    if not text:
        return ""
    compressed = []
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            compressed.append(text[i - 1] + str(count))
            count = 1
    compressed.append(text[-1] + str(count))
    return "".join(compressed)

if __name__ == '__main__':
    sample_string = "AAABBBCCDAAA"
    result = run_length_encode(sample_string)
    print(result)