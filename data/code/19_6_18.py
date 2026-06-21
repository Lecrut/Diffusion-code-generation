def rle_encode_case_insensitive(text):
    if not text:
        return ""
    text = text.lower()
    result = []
    current_char = text[0]
    count = 1
    for i in range(1, len(text)):
        char = text[i]
        if char == current_char:
            count += 1
        else:
            result.append(f"{current_char}{count}")
            current_char = char
            count = 1
    result.append(f"{current_char}{count}")
    return "".join(result)

if __name__ == "__main__":
    sample_input = "AaBbBcCCd"
    encoded_result = rle_encode_case_insensitive(sample_input)
    print(encoded_result)