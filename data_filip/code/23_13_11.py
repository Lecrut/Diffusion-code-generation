def run_length_encode(text):
    if not text:
        return ''
    encoded = []
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            encoded.append(text[i - 1])
            if count > 1:
                encoded.append(str(count))
            count = 1
    encoded.append(text[-1])
    if count > 1:
        encoded.append(str(count))
    return ''.join(encoded)

if __name__ == '__main__':
    test_string = 'AAABBBCCD'
    result = run_length_encode(test_string)
    print(result)