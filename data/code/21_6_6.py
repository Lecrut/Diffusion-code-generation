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
            result.append(f'{current_char}{count}')
            current_char = char
            count = 1
    result.append(f'{current_char}{count}')
    return ''.join(result)

if __name__ == '__main__':
    print(run_length_encode('aaabbc'))
    print(run_length_encode('abcdef'))
    print(run_length_encode('aaaaaa'))
    print(run_length_encode(''))
    print(run_length_encode('a'))