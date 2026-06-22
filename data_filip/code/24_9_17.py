def run_length_encode(text):
    if not text:
        return ''

    result = []
    current_char = text[0]
    count = 1

    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            result.append(str(count))
            result.append(current_char)
            current_char = text[i]
            count = 1

    result.append(str(count))
    result.append(current_char)

    return ''.join(result)

if __name__ == '__main__':
    sample_text = 'aaabbc'
    compressed = run_length_encode(sample_text)
    print(compressed)