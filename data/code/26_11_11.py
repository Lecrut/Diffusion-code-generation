def run_length_encode(text):
    if not text:
        return []
    result = []
    count = 1
    current_char = text[0]
    for i in range(1, len(text)):
        char = text[i]
        if char == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = char
            count = 1
    result.append((current_char, count))
    return result

if __name__ == '__main__':
    input_string = 'AAAABBBCCDAA'
    encoded = run_length_encode(input_string)
    print(encoded)