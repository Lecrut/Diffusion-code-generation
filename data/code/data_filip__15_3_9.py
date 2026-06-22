def compress_string(s):
    if not s: return ''
    result, current_char, count = '', s[0], 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            result += f'{current_char}{count}'
            current_char, count = char, 1
    return f'{result}{current_char}{count}'

if __name__ == '__main__':
    print(compress_string('bbbaaa'))