def rle_encode_case_insensitive(text):
    if not text:
        return ""
    lower_text = text.lower()
    result = []
    current_char = lower_text[0]
    count = 1
    for i in range(1, len(lower_text)):
        if lower_text[i] == current_char:
            count += 1
        else:
            if count > 1:
                result.append(str(count))
            result.append(current_char)
            current_char = lower_text[i]
            count = 1
    if count > 1:
        result.append(str(count))
    result.append(current_char)
    return "".join(result)

if __name__ == '__main__':
    sample_input = "AAABBBccDdd"
    result = rle_encode_case_insensitive(sample_input)
    print(result)