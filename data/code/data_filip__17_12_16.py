def run_length_encode_sequence(text):
    result = {}
    if not text:
        return result
    i = 0
    n = len(text)
    while i < n:
        char = text[i]
        if not char.isalnum():
            i += 1
            continue
        count = 0
        current_char = char
        while i < n and text[i] == current_char:
            count += 1
            i += 1
        if current_char in result:
            result[current_char].append(count)
        else:
            result[current_char] = [count]
    return result

if __name__ == '__main__':
    sample_input = "aaabbcc1112233a"
    encoded_data = run_length_encode_sequence(sample_input)
    print(encoded_data)