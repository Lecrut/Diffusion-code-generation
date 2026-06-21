def run_length_encode(s):
    if not s:
        return ''

    result = []
    count = 1
    prev_char = s[0]

    for i in range(1, len(s)):
        current_char = s[i]
        if current_char == prev_char:
            count += 1
        else:
            result.append(prev_char + str(count))
            prev_char = current_char
            count = 1

    result.append(prev_char + str(count))
    return ''.join(result)

if __name__ == '__main__':
    sample_inputs = [
        '',
        'a',
        'aa',
        'aab',
        'aabcccccaaa',
        'abc',
        'AAAAAAAAAABBBBCCCCC',
        'aabbcc',
        'xyz',
        'zzzzzzzzzzzzzzzzzzzz'
    ]
    for sample in sample_inputs:
        print(run_length_encode(sample))