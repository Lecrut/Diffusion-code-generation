def run_length_encode(text):
    if not text:
        return ""
    encoded = []
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            encoded.append(str(count) + text[i - 1])
            count = 1
    encoded.append(str(count) + text[-1])
    return "".join(encoded)

if __name__ == '__main__':
    sample_string = 'AAABBBCCCC'
    result = run_length_encode(sample_string)
    print(result)