def run_length_encode(text):
    if not text:
        return []
    result = []
    current_char = text[0]
    count = 1
    for index in range(1, len(text)):
        char = text[index]
        if char == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = char
            count = 1
    result.append((current_char, count))
    return result

if __name__ == '__main__':
    test_string = "aaabbccccddeeef"
    encoded_list = run_length_encode(test_string)
    print(encoded_list)