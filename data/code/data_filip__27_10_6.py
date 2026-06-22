def run_length_encode(s):
    if not s:
        return ''

    result = []
    current_char = s[0]
    count = 1

    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(current_char)
            result.append(str(count))
            current_char = char
            count = 1

    result.append(current_char)
    result.append(str(count))

    return ''.join(result)

if __name__ == '__main__':
    samples = ['AABBBCCC', 'ABC', 'AAAAA', 'ABABAB', '', '123123']
    for sample in samples:
        print(run_length_encode(sample))