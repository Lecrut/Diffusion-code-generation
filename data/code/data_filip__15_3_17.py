def compress_string(s):
    if not s:
        return ''
    result, count, current_char = [], 1, s[0]
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(f'{count}{current_char}')
            current_char, count = char, 1
    result.append(f'{count}{current_char}')
    return ''.join(result)

if __name__ == '__main__':
    sample_input = 'bbbaaa'
    print(compress_string(sample_input))