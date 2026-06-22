def encode_repeated_elements(s):
    if not s:
        return ''
    result = []
    current_char = s[0]
    count = 1
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result.append(f'{current_char}{count}')
            current_char = s[i]
            count = 1
    result.append(f'{current_char}{count}')
    return ''.join(result)

if __name__ == '__main__':
    print(encode_repeated_elements('aaabbbcc'))
    print(encode_repeated_elements('abcd'))
    print(encode_repeated_elements('a'))
    print(encode_repeated_elements(''))
    print(encode_repeated_elements('aaaaa'))