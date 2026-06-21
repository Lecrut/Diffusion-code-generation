def compress_text(text):
    if not text:
        return ""
    result = []
    current_char = text[0]
    count = 1
    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            if count > 1:
                result.append(current_char + str(count))
            else:
                result.append(current_char)
            current_char = text[i]
            count = 1
    if count > 1:
        result.append(current_char + str(count))
    else:
        result.append(current_char)
    return "".join(result)

if __name__ == '__main__':
    sample_input = "aaabbbccdddda"
    print(compress_text(sample_input))