def encode_run_length(text):
    if not text:
        return ""
    result = []
    count = 1
    current_char = text[0]
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = char
            count = 1
    result.append(f"{current_char}{count}")
    return "".join(result)

if __name__ == "__main__":
    sample_input = "aaabbbcccaaa"
    print(encode_run_length(sample_input))