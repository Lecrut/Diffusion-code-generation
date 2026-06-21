def run_length_encode(text):
    if not text:
        return ""
    result = []
    count = 1
    current_char = text[0]
    for index in range(1, len(text)):
        char = text[index]
        if char == current_char:
            count += 1
        else:
            result.append(f"{count}{current_char}")
            current_char = char
            count = 1
    result.append(f"{count}{current_char}")
    return "".join(result)

if __name__ == "__main__":
    sample_text = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    encoded_value = run_length_encode(sample_text)
    print(encoded_value)