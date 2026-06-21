def run_length_encode(text):
    if not text:
        return []
    result = []
    current_char = text[0]
    count = 1
    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            result.append(current_char)
            result.append(count)
            current_char = text[i]
            count = 1
    result.append(current_char)
    result.append(count)
    return result

if __name__ == '__main__':
    sample_string = "AAABBBCCDDDD"
    encoded_data = run_length_encode(sample_string)
    print(encoded_data)