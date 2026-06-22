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
            result.append(f'{count}{current_char}')
            current_char = char
            count = 1
    result.append(f'{count}{current_char}')
    return ''.join(result)

if __name__ == '__main__':
    sample1 = 'aabcccccaaa'
    sample2 = ''
    sample3 = 'abcdef'
    sample4 = 'aaaaa'
    sample5 = 'AABBCCDD'

    print(run_length_encode(sample1))
    print(run_length_encode(sample2))
    print(run_length_encode(sample3))
    print(run_length_encode(sample4))
    print(run_length_encode(sample5))