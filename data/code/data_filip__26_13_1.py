def encode(text):
    if not text:
        return ""
    result = []
    current_char = text[0]
    count = 1
    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = text[i]
            count = 1
    result.append(f"{count}{current_char}")
    return "".join(result)

if __name__ == "__main__":
    sample_string = "aaabbbcccaaa"
    encoded_result = encode(sample_string)
    print(encoded_result)