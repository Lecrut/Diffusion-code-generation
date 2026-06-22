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
            result.append(f"{current_char}{count}")
            current_char = lower_text[i]
            count = 1
    result.append(f"{current_char}{count}")
    return ''.join(result)

if __name__ == '__main__':
    sample = "AAABBBCccDdE"
    print(rle_encode_case_insensitive(sample))