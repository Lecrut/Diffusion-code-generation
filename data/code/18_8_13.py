def encode_run_length():
    text = "aabcccccaaa"
    if not text:
        return []
    result = []
    current_char = text[0]
    count = 1
    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(current_char)
            result.append(str(count))
            current_char = char
            count = 1
    result.append(current_char)
    result.append(str(count))
    return result

if __name__ == '__main__':
    print(encode_run_length())