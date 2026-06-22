def run_length_encoding(text):
    if not text:
        return ""
    result = []
    count = 1
    current_char = text[0]
    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            result.append(str(count) + current_char)
            current_char = text[i]
            count = 1
    result.append(str(count) + current_char)
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbbcccccdde"
    encoded_output = run_length_encoding(sample_input)
    print(encoded_output)