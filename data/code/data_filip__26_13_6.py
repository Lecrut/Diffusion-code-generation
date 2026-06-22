def run_length_encode(s: str) -> str:
    if not s:
        return ''
    encoded = []
    count = 1
    current_char = s[0]
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append(f'{current_char}{count}')
            current_char = char
            count = 1
    encoded.append(f'{current_char}{count}')
    return ''.join(encoded)
if __name__ == '__main__':
    sample_string = 'aaabbcdddd'
    result = run_length_encode(sample_string)
    print(result)