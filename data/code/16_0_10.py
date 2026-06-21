def run_length_encode(text):
    if not text:
        return ""
    result = []
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            result.append(str(count))
            result.append(text[i - 1])
            count = 1
    result.append(str(count))
    result.append(text[-1])
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbcccc"
    encoded_output = run_length_encode(sample_input)
    print(encoded_output)